def nicks(forms):
    
    names = []
    for form in forms:
        names.append(form[1])

    result = []
    for i in range(len(forms)):
        for j in range(len(forms[i])):
            for k in range(len(names) - 1):
                if k == i:
                    continue
                if forms[i][1][j:j+2] in names[k]:
                    result.append(forms[i][0])
                    break
    return result

forms = [ ["jm@email.com", "제이엠"], ["jason@email.com", "제이슨"], ["woniee@email.com", "워니"], ["mj@email.com", "엠제이"], ["nowm@email.com", "이제엠"] ]
result = nicks(forms)
print(result)