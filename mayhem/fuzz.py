#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    from num2words import num2words

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    toArgs = ['cardinal', 'ordinal', 'ordinal_num', 'year', 'currency']
    langArgs = [
        'en', 'am', 'ar', 'cz', 'de', 'dk', 
        'en_GB', 'en_IN', 'es', 'es_CO', 'es_VE', 
        'eu', 'fa', 'fi', 'fr', 'fr_CH', 'fr_BE', 
        'fr_DZ', 'he', 'hu', 'id', 'it', 'ja', 'kn', 
        'ko', 'kz', 'lt', 'lv', 'no', 'pl', 'pt', 'pt_BR',
        'sl', 'sr', 'sv', 'ro', 'ru', 'te', 'tg', 'tr',
        'th', 'vi', 'nl', 'uk'
    ]

    num = fdp.ConsumeFloatInRange(-10000, 10000)
    toArg = fdp.PickValueInList(toArgs)
    langArg = fdp.PickValueInList(langArg)
    num2words(num, to=toArg, lang=langArg)

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == "__main__":
    main()