% Pokemon Expert System
% DATABASE
:- dynamic gejala_pos/1.
:- dynamic gejala_neg/1.
% FAKTA & ATURAN
penyakit("Bun").
penyakit("Paralysis").
penyakit("Poison").
penyakit("Freeze").
penyakit("Overheat").
penyakit("Confusion").
penyakit("Fatigue").

gejala(suhu_tubuh_tinggi, "Bun").
gejala(luka_bakar_dikulit, "Bun").
gejala(penurunan_kekuatan_serangan, "Bun").
gejala(gerakan_melambat, "Bun").

gejala(gerakan_melambat, "Paralysis").
gejala(tidak_bisa_menyerang, "Paralysis").
gejala(susah_bergerak, "Paralysis").
gejala(penurunan_kekuatan_serangan, "Paralysis").

gejala(warna_kulit_ungu, "Poison").
gejala(muntah, "Poison").
gejala(kehilangan_hp_terus, "Poison").
gejala(terlihat_lemas, "Poison").

gejala(suhu_tubuh_rendah, "Freeze").
gejala(tubuh_membeku, "Freeze").
gejala(gerakan_melambat, "Freeze").
gejala(tidak_bisa_menyerang, "Freeze")

gejala(suhu_tubuh_tinggi, "Overheat").
gejala(gerakan_melambat, "Overheat").
gejala(kehilangan_fokus, "Overheat").
gejala(penurunan_kekuatan_serangan, "Overheat").

gejala(kehilangan_fokus, "Confusion").
gejala(tidak_bisa_menyerang, "Confusion").
gejala(sering_menyerang_sendiri, "Confusion").
gejala(penurunan_kekuatan_serangan, "Confusion").

gejala(gerakan_melambat, "Fatigue").
gejala(kehilangan_fokus, "Fatigue").
gejala(terlihat_lemas, "Fatigue").
gejala(tidak_bisa_menyerang, "Fatigue").

pertanyaan(suhu_tubuh_tinggi, Y) :-
Y = "Apakah suhu tubuh tinggi?".
pertanyaan(luka_bakar_dikulit, Y) :-
Y = "Apakah ada luka bakar di kulit?".
pertanyaan(penurunan_kekuatan_serangan, Y) :-
Y = "Apakah ada penurunan kekuatan serangan?".
pertanyaan(gerakan_melambat, Y) :-
Y= "Apakah gerakan melambat?".
pertanyaan(tidak_bisa_menyerang, Y) :-
Y = "Apakah tidak bisa menyerang?".
pertanyaan(susah_bergerak, Y) :-
Y = "Apakah susah bergerak?".
pertanyaan(warna_kulit_ungu, Y) :-
Y = "Apakah warna kulit ungu?".
pertanyaan(muntah, Y) :-
Y = "Apakah muntah?".
pertanyaan(kehilangan_hp_terus, Y) :-
Y = "Apakah kehilangan HP terus menerus?".
pertanyaan(tubuh_membeku, Y) :-
Y = "Apakah tubuh membeku?".
pertanyaan(suhu_tubuh_rendah, Y) :-
Y = "Apakah suhu tubuh rendah?".
pertanyaan(kehilangan_fokus, Y) :-
Y = "Apakah kehilangan fokus?".
pertanyaan(sering_menyerang_sendiri, Y) :-
Y = "Apakah sering menyerang sendiri?".
pertanyaan(terlihat_lemas, Y) :-
Y = "Apakah terlihat lemas?".
