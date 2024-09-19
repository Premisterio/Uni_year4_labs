import os
from google.cloud import translate_v2 as translate

# Посилання на мій API ключ
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/Users/premisterio/Documents/Файли/Інші файли/Google Translate API/empyrean-willow-435911-b7-388878703184.json"
translate_client = translate.Client()


def load_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = {'text_file': file.readline().strip(), 'target_language': file.readline().strip(),
                      'output_mode': file.readline().strip(), 'max_chars': int(file.readline().strip()),
                      'max_words': int(file.readline().strip()), 'max_sentences': int(file.readline().strip())}
        return config
    except Exception as e:
        print(f"Error loading config file: {e}")
        return None


def count_words_sentences(text):
    words = text.split()
    sentences = text.split('.')
    return len(words), len(sentences)


def read_text_file(file_path, max_chars, max_words, max_sentences):
    try:
        with open(file_path, 'r') as file:
            text = ""
            total_chars = 0
            total_words = 0
            total_sentences = 0

            for line in file:
                if total_chars >= max_chars or total_words >= max_words or total_sentences >= max_sentences:
                    break
                text += line
                total_chars += len(line)
                words_in_line, sentences_in_line = count_words_sentences(line)
                total_words += words_in_line
                total_sentences += sentences_in_line

            return text.strip(), total_chars, total_words, total_sentences
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
        return None, 0, 0, 0


def detect_language(text):
    try:
        result = translate_client.detect_language(text)
        return result['language']
    except Exception as e:
        print(f"Error in language detection: {e}")
        return None


def translate_text(text, target_language):
    try:
        result = translate_client.translate(text, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        print(f"Error in translation: {e}")
        return None


def save_translation(file_name, translated_text, target_language_code):
    try:
        output_file = f"{os.path.splitext(file_name)[0]}_{target_language_code}.txt"
        with open(output_file, 'w') as file:
            file.write(translated_text)
        print("Ok")
    except Exception as e:
        print(f"Error saving translation to file: {e}")


def main():
    config = load_config('config.txt')
    if not config:
        return

    # Читаємо текстовий файл і отримуємо потрібні дані
    text, char_count, word_count, sentence_count = read_text_file(
        config['text_file'], config['max_chars'], config['max_words'], config['max_sentences']
    )

    if not text:
        print(f"Error: No text to translate.")
        return

    # Виводимо інформацію про файл
    print(f"File: {config['text_file']}")
    print(f"Characters: {char_count}")
    print(f"Words: {word_count}")
    print(f"Sentences: {sentence_count}")

    # Визначаємо мову тексту
    detected_language = detect_language(text)
    if not detected_language:
        print("Error: Could not detect language.")
        return

    print(f"Detected language: {detected_language}")

    # Переклад тексту
    translated_text = translate_text(text, config['target_language'])
    if not translated_text:
        print("Error: Could not translate text.")
        return

    # Виведення результату
    if config['output_mode'] == 'screen':
        print(f"Translated to {config['target_language']}:")
        print(translated_text)
    elif config['output_mode'] == 'file':
        save_translation(config['text_file'], translated_text, config['target_language'])
    else:
        print("Error: Invalid output mode in config.")


if __name__ == "__main__":
    main()
