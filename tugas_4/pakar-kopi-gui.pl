% Minuman Kopi
% DATABASE
:- dynamic rekomen_pos/1.
:- dynamic rekomen_neg/1.
% FAKTA & ATURAN
kopi("Caffe Latte").
kopi("Americano").
kopi("Es Kopi Gula Aren").
kopi("Cappuccino").
rekomen(panas, "Caffe Latte").
rekomen(susu, "Caffe Latte").
rekomen(tidak_pahit, "Caffe Latte").
rekomen(panas, "Americano").
rekomen(tanpa_susu, "Americano").
rekomen(pahit, "Americano").
rekomen(dingin, "Es Kopi Gula Aren").
rekomen(susu, "Es Kopi Gula Aren").
rekomen(sedang_pahit, "Es Kopi Gula Aren").
rekomen(manis, "Es Kopi Gula Aren").
rekomen(panas, "Cappuccino").
rekomen(susu, "Cappuccino").
rekomen(sedang_pahit, "Cappuccino").
rekomen(tidak_manis, "Cappuccino").
rekomen(berbuih, "Cappuccino").

pertanyaan(panas, Y) :-
    Y = "Apakah Anda ingin kopi panas?".

pertanyaan(dingin, Y) :-
    Y = "Apakah Anda ingin kopi dingin?".

pertanyaan(susu, Y) :-
    Y = "Apakah Anda suka kopi dengan susu?".

pertanyaan(tanpa_susu, Y) :-
    Y = "Apakah Anda ingin kopi tanpa susu?".

pertanyaan(tidak_pahit, Y) :-
    Y = "Apakah Anda tidak suka kopi yang pahit?".

pertanyaan(pahit, Y) :-
    Y = "Apakah Anda suka kopi pahit?".

pertanyaan(sedang_pahit, Y) :-
    Y = "Apakah Anda suka kopi dengan rasa pahit sedang?".

pertanyaan(manis, Y) :-
    Y = "Apakah Anda suka kopi manis?".

pertanyaan(tidak_manis, Y) :-
    Y = "Apakah Anda tidak suka kopi yang manis?".

pertanyaan(berbuih, Y) :-
    Y = "Apakah Anda suka kopi dengan busa di atasnya?".