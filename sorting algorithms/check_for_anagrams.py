def anagram(A,B):
    letters = [0 for _ in range(26)]
    for i in range(len(A)):
        letters[ord(A[i])-97] += 1
        letters[ord(B[i])-97] -= 1
    for i in range(26):
        if letters[i] != 0:
            return False
    return True

print(anagram('antek','ketne'))