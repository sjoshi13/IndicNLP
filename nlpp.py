# The path to the local git repo for Indic NLP library
INDIC_NLP_LIB_HOME=r"C:\Users\ASUS\Documents\src\indic_nlp_library"

# The path to the local git repo for Indic NLP Resources
INDIC_NLP_RESOURCES=r"C:\Users\ASUS\Documents\src\indic_nlp_resources"
import sys
sys.path.append(r'{}\src'.format(INDIC_NLP_LIB_HOME))
from indicnlp import common
common.set_resources_path(INDIC_NLP_RESOURCES)
from indicnlp import loader
loader.load()
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

input_text="\u0958 \u0915\u093c"
remove_nuktas=False
factory=IndicNormalizerFactory()
normalizer=factory.get_normalizer("hi",remove_nuktas)
output_text=normalizer.normalize(input_text)

print(output_text)
print('Length before normalization: {}'.format(len(input_text)))
print('Length after normalization: {}'.format(len(output_text)))
from indicnlp.transliterate.unicode_transliterate import UnicodeIndicTransliterator
input_text='राजस्थान'
# input_text='രാജസ്ഥാന'
# input_text='රාජස්ථාන'
print(UnicodeIndicTransliterator.transliterate(input_text,"hi","ta"))
