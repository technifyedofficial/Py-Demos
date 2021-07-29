def sales_profit(sp , cp , q):
    formula = str((sp - cp) * q)
    total_cp = str(q * cp)
    total_sp = str(q * sp)
    print('For ' + str(q) + ' total cost price is ' + total_cp + ' rupees')
    print('For ' + str(q) + ' total selling price is ' + total_sp + ' rupees')
    print('Your total profit made is ' + formula + ' rupees')

