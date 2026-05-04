class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        flag = False
        for ele in s:
            
            if ele in '({[':
                stack.append(ele)
                flag = False

            else:
                if len(stack) != 0:
                    top = stack.pop()
                    if (ele == ')' and top == '(') or (ele == '}' and top == '{') or (ele == ']' and top == '['):
                        flag = True
                    else:
                        flag = False
                        break

                else:
                    flag = False
                    break

        if flag == True and len(stack) == 0:
            return True
        else:
            return False
