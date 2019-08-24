def stringCompression(text):
      index = 0
      resp = ""
      while len(text) > index:
            count = 0
            while len(text) > (index + count) and text[index] == text[index + count]:
                  count += 1
            resp += text[index] + str(count) 
            index += count

      return resp