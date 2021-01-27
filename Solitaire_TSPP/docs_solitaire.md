Solitaire Pyramid | Пасьянс (Пирамида)
-

#### Rules:
EN: 

1. To set up the pyramid, one card is dealt face up at the top of the playing area,
then two cards beneath and partially covering it, then three beneath them,
and so on completing with a row of seven cards for a total of 28 cards dealt (or six rows of 21 cards).
The remaining cards are placed to the side face down, and make up the Stock.

2. To play, pairs of exposed cards can be removed to the foundation if their values total 13.
Thus, kings can be removed immediately to the foundation. 
In order to be removed, cards must not be covered, so when an Ace rests on a Queen, that Queen can not be removed.

3. You may draw cards from the stock one at a time and match it with any exposed card.
If no match is made the drawn stock card is still discarded into the foundation.
Once the stock is exhausted and/or no more pairs can be made, the game ends.

4. To score, count the number of remaining face up cards in the pyramid.
A perfect score is therefore zero, where all cards have been matched into the Foundation.

5. To be considered won, all cards (cards from the pyramid and cards from the stock) must be moved to the foundation; 
the game cannot be won if at least two cards cannot be moved from the stock.


RU: 
1. Чтобы построить пирамиду, одна карта сдается лицом вверх в верхней части игрового поля,
затем две карты под ней и частично закрывают ее, затем три под ними и так далее,
завершая ряд из семи карт, всего 28 карт. сдано (или шесть рядов по 21 карте).
Оставшиеся карты кладутся лицевой стороной вниз и составляют колоду.

2. Для игры пары открытых карт могут быть убраны в фундамент, если их значение составляет 13.
Таким образом, короли могут быть немедленно удалены в фундамент.
Чтобы удалить карты, карты не должны быть закрыты, поэтому,
когда туз лежит на даме, эта королева не может быть удалена.

3. Вы можете брать карты из колоды по одной и сравнивать ее с любой открытой картой.
Если совпадений нет, вытянутая карта запаса все равно сбрасывается в фонд.
Когда запас исчерпан и / или больше невозможно собрать пары, игра заканчивается.

4. Чтобы набрать очки, подсчитайте количество оставшихся открытых карт в пирамиде.
Таким образом, идеальный балл равен нулю, если все карты были подобраны для Фонда

5. Чтобы считаться выигранными, все карты (карты из пирамиды и карты из колоды) должны быть перемещены на фундамент;
 игра не может быть выиграна, если по крайней мере две карты нельзя переместить из колоды.

Design Pattern
-

Behavioral pattern.

1. Observer
2. Iterator
3. State

4. Singleton(?)

 Classes
-

 * Card
 * Deck
 * PyramidBoard or SolitaireBoard
 * Foundation
 
---

Class **Card**:


_params_: 
````
card_value: list of strings
suit:       list of strings
is_flipped: boolean
````

_methods_: 
````
__init__(): card_obj => void: 
init params

is_flipped() => boolean:
returns boolean value whether the card is faced up or not

flip() => void:
face the card up or down
````
 


---

Class **Deck**: 

_params_: 

````
cards: []
deck: []
````

_methods_: 
````
fill_deck(): deck_obj => void
 
shuffle() deck_obj => void


````


