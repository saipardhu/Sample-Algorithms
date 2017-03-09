a1=['aa','ab','eat','a']
a2=['bb','ba','oat','bb']
result =[]
for it in range(len(a1)):
    a1_dict = {}
    a2_dict = {}
    elem_a1 = list(a1[it])
    elem_a2 = list(a2[it])
    elem_a1.sort()
    elem_a2.sort()
    for i in elem_a1:
        if i in a1_dict:
            a1_dict[i] += 1;
        else:
            a1_dict[i] = 1;
    # if(len(elem_a1)!=len(elem_a2)): result.append(-1)
    # result.append(len(list(elem_a1)-list(elem_a2)))
    for i in elem_a2:
        if i in a2_dict:
            a2_dict[i] += 1;
        else:
            a2_dict[i] = 1;
    print(a1_dict, a2_dict)
     for key,val in a1_dict.items:
        if (val != o_list[key]):
