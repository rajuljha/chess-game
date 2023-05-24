# Chess-jail 🌟

## Rules ✨
1. Any cell on the chess board can have a secret key hidden in it.
2. You and your friend are trapped in jail, and you know where the key is hidden.
3. You have to convey to your friend where the hidden key is on the chess baord.
4. Each cell has a coin with either tails or heads. 
5. You can flip only one coin on the chess board to convey where the key lies to your friend.
6. You can preplan and discuss strategy with your friend. But adter you know about the key, you both can't be present in the jail cell at the same time.

## How will you escape the jail? 🕷️ 


## Open the game ✨
1. Clone the repo, navigate to chess-game, and open chess_game.py
```python
python chess_game.py
```

## What this program does? 🎯

1. A pictorial representation of the problem is shown here. <br> ![Screenshot 2023-05-24 at 2 52 31 PM](https://github.com/rajuljha/chess-game/assets/34140028/d74e788b-2a5b-4cfd-a0ea-5ac6e21548f9)

2. When you click on the Buttons labelled part 1 to part 6, particular regions of the chess board will be highlited as follows:
  1. Even numbered columns <br> ![Screenshot 2023-05-24 at 2 52 50 PM](https://github.com/rajuljha/chess-game/assets/34140028/1e09a970-d6b4-4487-917a-ee7cc262a201)
    
  2. 3rd,4th and 7th,8th columns <br> ![Screenshot 2023-05-24 at 2 53 02 PM](https://github.com/rajuljha/chess-game/assets/34140028/fcb58147-f37a-4d2f-8680-2dcc5166a256)

  3. Right four columns  <br> ![Screenshot 2023-05-24 at 2 53 12 PM](https://github.com/rajuljha/chess-game/assets/34140028/a38cdd57-c277-4b29-bb87-02f774e03824)
  
  4. Even numbered rows <br> ![Screenshot 2023-05-24 at 2 53 21 PM](https://github.com/rajuljha/chess-game/assets/34140028/dd60652f-c9bb-44e9-b9fb-094c0e08742f)

  5. 3rd,4th and 7th,8th rows <br> ![Screenshot 2023-05-24 at 2 53 34 PM](https://github.com/rajuljha/chess-game/assets/34140028/9652f260-e126-430e-a6ac-6739094a12bb)

  6. Bottom 4 rows <br> ![Screenshot 2023-05-24 at 2 53 43 PM](https://github.com/rajuljha/chess-game/assets/34140028/5ea8cb57-e49e-40b8-93a4-28b6043dc87f)

3. When a cell is clicked, the position of the cell is displayed, and binary representaiton (6 digits) of the cell is also displayed in the command line.
4. The board's parity is displayed when any of the buttons Part 1 - Part 6 are clicked. <br> ![Screenshot 2023-05-24 at 2 54 40 PM](https://github.com/rajuljha/chess-game/assets/34140028/81095a40-44e6-462e-8c5a-ccdfdaa70d92) 
5. Then an XOR operation is performed on the cell binary representaion and board parity binary to obtain the binary result of which coin should be flipped.
6. Then that result is converted to number and the program tells us which coin should be flipped by us to win the game. <br>
![Screenshot 2023-05-24 at 3 27 17 PM](https://github.com/rajuljha/chess-game/assets/34140028/d0e24ca4-bfe6-4933-9ae0-bc81c4a81cae)

## References
1. 3blue1brown youtube channel: Video https://www.youtube.com/watch?v=wTJI_WuZSwE&t=208s
2. Stand Up Maths: Video https://www.youtube.com/watch?v=as7Gkm7Y7h4
3. Article (http://datagenetics.com/blog/december12014/index.html by DataGenetics
