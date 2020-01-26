def open():
  print("--NUMPAD--\n")
  print("1\t2\t3\t\n4\t5\t6\t\n7\t8\t9\t\n\t0")
  num=int(input("Enter Any Number:"))
  contact_list={'Customer Care':121,'Police':911}
  key_list=list(contact_list.keys())
  value_list=list(contact_list.values())
  if num in value_list:
    print(key_list[value_list.index(num)])
  else:
    info=input("If you want to create a new contact... Press Y or N:")
    if(info=='y' or info=='Y'):
      name=input('Enter the name of contact:')
      contact_list.update({name:num})
      print("Contact Added Successfully!")

open()
