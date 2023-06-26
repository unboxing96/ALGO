def solution(today, terms, privacies):
    answer = []

    today_year, today_month, today_day = map(int, today.split("."))
    terms_dict = {term.split()[0]: int(term.split()[1]) for term in terms}

    for i in range(len(privacies)):
        privacy_date, privacy_term = privacies[i].split()
        privacy_year, privacy_month, privacy_day = map(int, privacy_date.split("."))
        
        expiration_month = (privacy_month - 1 + terms_dict[privacy_term]) % 12 + 1
        expiration_year = privacy_year + (privacy_month - 1 + terms_dict[privacy_term]) // 12

        if (today_year, today_month, today_day) >= (expiration_year, expiration_month, privacy_day):
            answer.append(i + 1)
    
    return answer