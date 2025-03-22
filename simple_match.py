#!/usr/bin/env python3

# Для каждого регулярного выражения, которое требуется написать,
# указаны строки, соответствующие этому выражению (они отмечены знаком +),
# а также строки, не соответствующие этому выражению (отмечены знаком -)

# + a
# + ab
# - b
# - ba
REGEXP_1 = r'^a(b)?$'

# + aab
# + abb
# + acb
# - ab
# - aabc
REGEXP_2 = r'^a[a-z]{2}$'

# + sofia.mp3
# + sofia.mp4
# - sofia.mp7
# - sofia.mp34
REGEXP_3 = r'^sofia\.mp[34]$'

# + taverna
# + versus
# + vera
# + zveri
# - zver
REGEXP_4 = r'^[a-z]*ver[a-z]+$'

# - a
# - aa
# + aaa
# - aaaa
# - b
# - bb
# + bbb
# - bbbb
# - ccc
REGEXP_5 = r'^(aaa|bbb)$'

# - Ok
# - OkOk
# + OkOkOk
# - OkOkOkOk
# - ab
# - abab
# + ababab
# - abababab
REGEXP_6 = r'^(Ok{2}Ok|ab{2}ab)$'

# - aaa
# - aaa aaa
# + aaa Aaa aaa
# + aaa aaa Aaa
# + Aaa aaa aaa
# - A
# - aaa A aaa
REGEXP_7 = r'([aA]aa\s){2}[aA]aa'

# + abc
# + abc03
# + a-b-c-3
# + a.b.c.0
# - Aabc
# - abc1
# - #abc
REGEXP_8 = r'^[a-z][a-z0-9.-]*$'
