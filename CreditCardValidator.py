def validate_credit_card(card_number):
    card_number = card_number.replace(" ", "")
    if not card_number.isdigit():
        return False
    
    sum_val = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    
    for count in range(num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven ):
            digit = digit * 2
        if digit > 9:
            tobin =  It . was even possible. Therefore, even Computer
