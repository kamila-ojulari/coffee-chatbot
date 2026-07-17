def coffee_bot():
  print("Welcome to the cafe!")

  size = get_size()
  drink_type = get_drink_type()
  print(f"Alright, that's a {size} {drink_type}!")
  name = input("Can I get your name please? \n> ")
  print("Thanks, " + name + " your drink will be ready shortly.")
  total_price = price_tag(size, drink_type)
  print(f"That'd be ${total_price} bucks!")
def get_size():
  res = input('What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
  

  if res == 'a':
    return 'small'
  elif res == 'b':
    return 'medium'
  elif res == 'c':
    return 'large'
  else:
    print_message()
    return get_size()
    
def print_message():
  print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")    

def get_drink_type():
  res = input("What type of drink would you like?\n[a] Brewed Coffee\n[b] Mocha\n[c] Latte\n> ") 
  
  if res == 'a':
    return 'brewed coffee'
  elif res == 'b':
    return 'mocha'
  elif res == 'c':
    return order_latte()
  else:
    print_message()
    return get_drink_type()

def order_latte():
  res = input("And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")

  if res == 'a':
    return 'latte'
  elif res == 'b':
    return 'non-fat'
  elif res == 'c':
    return 'soy latte'
  else:
    print_message()
    return order_latte()

def price_tag(size, drink_type):
  price = 0.0
  if size == 'small':
    price += 3.00
  elif size == 'medium':
    price += 4.00
  elif size == 'large':
    price += 5.00    

  if drink_type == 'brewed coffee':
    price += 1.00
  elif drink_type == 'mocha':
    price += 0.75
  else:
    price += 0.50      
  return price
coffee_bot()