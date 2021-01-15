def matchingWords(sentence1, sentence2):
    words1 = sentence1.strip().split(" ")
    words2 = sentence2.strip().split(" ")
    score = 0
    for word1 in words1:
        for word2 in words2:
            if word1.lower() == word2.lower():
                score += 1
    return score
if __name__ == "__main__":
    print("\n\n\tWelcome to the Search Engine : Made by --> @Satyam Tripathi & Company\n")
    sentences = ["python is a good", "this is snake",
                 "harry is a good boy", "satyam tripathi belong to mahoba uttar pradesh","This is pycharm"]
    query = input("Please Enter the String you want to Search :  ")
    scores = [matchingWords(query, sentence) for sentence in sentences]
    a=sorted(zip(scores, sentences), reverse=True)
    sortedSentScore = [i for i in a if i[0]!=0]
    print(f"\n\t\t\t{len(sortedSentScore)} results found !!\n")
    for score, item in sortedSentScore:
        print(f" \"{item.upper()}\"  :  with a score of {score}")

