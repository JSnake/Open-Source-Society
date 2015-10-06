s = "azcbobobegghakl"
longest_substring = ""

for i in xrange(len(s)):
    for j in xrange(i + 1, len(s)):
        index = s[i:j + 1]
        if "".join(sorted(index)) == index:
            longest_substring = max(longest_substring, index, key=len)
        else:
            break

print "Longest substring in alphabetical order is: ", longest_substring