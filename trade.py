import random

p = ["diamond", "gold"]

balance = 350
diamond = 400
gold = 250

while True:
 print('ВНИМАНИЕ ПИШИТЕ ВСЕ ОТВЕТЫ С БОЛЬШОЙ БУКВЫ! ИНАЧЕ КОД ПРИДЕТСЯ ПЕРЕЗАПУСКАТЬ')
 a=input('Что вы хотите выбрать Алмаз, золото или ждать пока опустится цена? Алмаз\Золото\Ждать ')
 while True:
   if a == 'Ждать':
       diamond = diamond + random.choice(range(-35, 35))
       gold = gold + random.choice(range(-10, 10))
       print('Цены спустя день:')
       print('Алмаз ' + str(diamond))
       print('Золото ' + str(gold))
       frist = input('Ждать ещё или назад? Ждать\Назад ')
       while True:
           if frist == 'Ждать':
               diamond = diamond + random.choice(range(-35, 35))
               gold = gold + random.choice(range(-10, 10))
               print('Цены спустя день:')
               print('Алмаз ' + str(diamond))
               print('Золото ' + str(gold))
               frist = input('Ждать ещё или назад? Ждать\Назад ')
           if frist == 'Назад':
              break
       break
   if a == 'Алмаз':
       print('На вашем счету ' + str(float(balance)) + ' $')
       print('На данный момент Алмаз стоит ' + str(int(diamond)) + ' $')
       order = input('Открыть ордер? Да\Нет ')
       while True:
           if order == 'Нет':
               break
           elif order == 'Да':
               while True:
                   if diamond > balance:
                       print('У вас недостаточно средств')
                       break
                   elif diamond <= balance:
                       balance = balance - diamond
                       print('Ваш баланс ' + str(balance) + ' $')
                       w = input('Вы открыли ордер на Алмаз, Что будете делать с ордером? Ждать\Закрыть ')
                       while True:
                           if w == 'Ждать':
                               diamond = diamond + random.choice(range(-35, 35))
                               gold = gold + random.choice(range(-10, 10))
                               print('Стоимость Алмаза ' + str(diamond))
                               w = input('Что будете делать с ордером? Ждать\закрыть ')
                           if w == 'Закрыть':
                               print('Стоимость Алмаза на момент закрытия ордера стоила ' + str(int(diamond)) + ' $')
                               balance = balance + diamond
                               print('Ваш баланс: ' + str(balance) + ' $')
                               break
                       break
               break
           break
       break
   elif a == 'Золото':
     print('На вашем счету ' + str(float(balance)) + ' $')
     print('На данный момент Золото стоит ' + str(int(gold)) + ' $')
     order = input('Открыть ордер? Да\нет')
     while True:
         if order == 'Нет':
             break
         elif order == 'Да':
             while True:
                 if gold > balance:
                     print('У вас недостаточно средств')
                     break
                 elif gold <= balance:
                     balance = balance - gold
                     print('Ваш баланс ' + str(balance) + ' $')
                     w = input('Вы открыли ордер на Золото, Что будете делать с ордером? Ждать\Закрыть ')
                     while True:
                         if w == 'Ждать':
                             gold = gold + random.choice(range(-10, 10))
                             diamond = diamond + random.choice(range(-35, 35))
                             print('Стоимость золота ' + str(gold))
                             w = input('Что будете делать с ордером? Ждать\Закрыть ')
                         if w == 'Закрыть':
                             print('Стоимость золота на момент закрытия ордера стоила ' + str(int(gold)) + ' $')
                             balance = balance + gold
                             print('Ваш баланс: ' + str(balance) + ' $')
                             break
                     break
             break
         break
     break
