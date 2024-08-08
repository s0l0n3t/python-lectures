#Sözlükler

dic_1 = {"data_1" : "0000",
        "data_2" : "0001" ,
        "data_3" : "0010" ,
        "data_4" : "0011" ,
        "data_5" : "0100" ,
        "data_6" : "0101" ,
        "data_7" : "0110" ,
        "data_8" : "0111" ,
        "data_9" : "1000" ,
        "data_10": "1001" ,
        "data_11": "1010" ,
        "data_12": "1011" ,
        "data_13": "1100" ,
        "data_14": "1101" ,
        "data_15": "1110" ,
        "data_16": "1111" ,
}

dic_2 = { 
    "list_1" : [0,1,2,3,4,5],
    "list_2" : ["data_1","data_2","data_3"]    
}
print(len(dic_1))
print((dic_2))

print(dic_1["data_1"],dic_1["data_2"],dic_2["list_1"][0])

dic_1["data_ex"] = "00001"

dic_2["list_1"] = ["changed_list",1,2,3,4]

print(dic_2)

dic_2[55] = "integer testi"

print(dic_2)

inside_tuple = ("0x0A",)

dic_2[inside_tuple] = "inside to tuple"
print(dic_2)