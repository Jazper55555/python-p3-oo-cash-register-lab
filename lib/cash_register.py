#!/usr/bin/env python3
class CashRegister:
  def __init__(self, discount=0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []
    self.transactions = []

  def add_item(self, item, price, quantity=1):
    self.total = (float(price) * quantity) + self.total
    multiple_items = [item] * quantity
    self.transactions += [(price * quantity)]
    self.items += multiple_items
    return self.total
  
  def apply_discount(self):
    if self.discount == 0:
      print('There is no discount to apply.')
    else:
      discount_percentage = self.discount / 100
      discounted_amount = self.total * discount_percentage
      self.total = int(self.total - discounted_amount)
      print(f"After the discount, the total comes to ${self.total}.")

  def void_last_transaction(self):
    if self.items == []:
      return self.total == 0
    else:
      last_transaction = self.transactions.pop()
      self.total -= last_transaction
      self.transactions.pop()
      return self.total