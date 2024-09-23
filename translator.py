import argostranslate.package
import argostranslate.translate

# Load and install the language package if needed
argostranslate.package.install_from_path("./app/translate-de_en-1_0.argosmodel")

# Read the file and use its content for translation
with open("./app/test.txt", mode="r", encoding="utf-8") as my_file:
    file_content = my_file.read()

# Translate the content of the file from German to English
translated_text = argostranslate.translate.translate(file_content, "de", "en")

# Open the file in append mode and write the translated text at the end
with open("./app/test.txt", mode="a", encoding="utf-8") as my_file:
    my_file.write("\n\n--- Translated Text ---\n")
    my_file.write(translated_text)

# Output the translated text
print(translated_text)




#
# import argostranslate.package
# import argostranslate.translate
# import os
#
# # Load and install the language package if needed
# argostranslate.package.install_from_path("./app/translate-de_en-1_0.argosmodel")
#
# # Define paths for original and translated files
# original_file_path = "./app/test.txt"
# translated_file_path = "./app/test_translated.txt"
#
# # Read the file and use its content for translation
# with open(original_file_path, mode="r", encoding="utf-8") as my_file:
#     file_content = my_file.read()
#
# # Translate the content of the file from German to English
# translated_text = argostranslate.translate.translate(file_content, "de", "en")
#
# # Create a new file and write the untranslated and translated text into it
# with open(translated_file_path, mode="w", encoding="utf-8") as translated_file:
#     translated_file.write("--- Original Text ---\n")
#     translated_file.write(file_content)
#     translated_file.write("\n\n--- Translated Text ---\n")
#     translated_file.write(translated_text)
#
# # Output the translated text
# print(f"Translated text written to {translated_file_path}")
#

