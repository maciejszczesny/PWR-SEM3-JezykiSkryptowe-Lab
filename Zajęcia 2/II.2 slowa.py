def slowa(rozdzielacz, *slowa):
    ciagZnakow = ""
    for slowo in slowa:
        ciagZnakow += slowo+rozdzielacz
    print(ciagZnakow)
    return ciagZnakow

slowa(" ;jjjj ","aaa","bbbbb","cc","d","ee","fff")
