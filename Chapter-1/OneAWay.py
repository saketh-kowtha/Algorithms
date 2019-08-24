def oneWay(pattern, text):
      def replace(str1, str2):
            verified = False
            for s1, s2 in zip(pattern, text):
                  if s1 != s2 :
                        if verified == True:
                              return False
                        verified = True
            return verified

      def insert(str1, str2):
            count = 0
            index = 0
            while index < len(str2):
                  if str1[index] != str2[index] :
                        count += 1
                  if count > 2 :
                        return False
                  index += 1

      if abs(len(pattern) - len(text)) > 2 :
            return False

      elif len(pattern) == len(text) :
            replace(pattern, text)
      elif len(pattern) > len(text) :
            insert(pattern, text)
      elif len(pattern) < len(text) :
            insert(text, pattern)