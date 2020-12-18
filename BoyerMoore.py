'''
 - Implementation of Boyer Moore Algorithm for Pattern Searching
   using both bad character and good suffix rules.

 - Created by : Khalid Gad
'''

class BoyerMoore:
    
    def __init__(self):
        pass

    def bad_char_heuristic(self, p, m):

        NO_OF_CHARS = 256

        bad_char = [-1]*NO_OF_CHARS

        for i in range(m):
            bad_char[ord(p[i])] = i

        return bad_char


    def GS_preprocess1(self, border, steps, p, m):

        i, j = m, m +1

        border[i] = j

        while i > 0:

            while j <= m and p[i-1] != p[j-1]:

                if steps[j] == 0:
                    steps[j] = j-i

                j = border[j]

            i -= 1
            j -= 1
            border[i] = j

    
    def GS_Preprocess2(self, border, steps, m):
        
        j = border[0]

        for i in range(m+1):

            if steps[i] == 0:
                steps[i] = j

            if i == j:
                j = border[j]


    def preprocess(self, p, m):

        bad_char = self.bad_char_heuristic(p, m)
        border = [0]*(m+1)
        steps = [0]*(m+1)
        self.GS_preprocess1(border, steps, p, m)
        self.GS_Preprocess2(border, steps, m)

        return bad_char, border, steps


    def search(self, text, pattern):

        occurrence = []

        t, n, p, m = text, len(text), pattern, len(pattern)

        bad_char, border, steps = self.preprocess(p, m)

        i = 0
        while i < n-m+1:

            j = m-1

            while j >= 0 and t[i+j] == p[j]:
                j -= 1
            
            if j < 0:
                occurrence.append(i)
                i += max(steps[0], (m-bad_char[ord(t[i+m])] if i+m<n else 1))

            else:
                i += max(steps[j+1],j-bad_char[ord(t[i+j])]) 

        return occurrence
        
def main():

    txt = input("txt : ")
    p = input("p : ")
    print(BoyerMoore().search(txt, p))


if __name__ == "__main__":
    main()