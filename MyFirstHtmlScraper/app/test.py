﻿# -*- coding: utf-8 -*-
import re
from functions import *

s = "Ten, który rozumie mężczyzn), prof. Gerhard Amendt (Kobiece parytety – parytetowe kobiety), Arne Hoffmann (Czy kobiety są lepszymi ludźmi? Drżenie mężczyzn, Ratujcie naszych synów! Jak blokuje się przyszłość chłopcom i jak możemy temu zaradzić), Bettina Peters ( Mężczyźni, brońcie się!), Christine Bauer-Jelinek (Fałszywy wróg: winni nie są mężczyźni), Matthias Matussek (Społeczeństwo bez ojców. Polemika przeciwko zniesieniu rodziny), Eckhard Kuhla (redaktor antologii tekstów maskulistycznych Ruch wyzwolenia mężczyzn), Astrid von Friesen (Winni są zawsze inni! Poporodowe bóle feminizmu. Sfrustrowane kobiety i milczący mężczyźni) , Beate Kricheldorf (Odpowiedzialność? Nie, dziękuję! Kobieca postawa ofiary jako strategia i taktyka), Kerstin Steinbach (Spojrzenie wstecz na feminizm – od początku kłamstwo przeciwko równości, logice i seksualnej przyjemności) , Peter Mersch, (Egalitarny feminizm – droga w ślepy zaułek), Heike Diefenbach (Patriarchat – znaczenie, empiryczna treść, polityczna instrumentalizacja), prof. Walter Hollstein (Co zostało z mężczyzny. Kryzys i przyszłość silnej płci)Michael Klein (Światopoglądowy terror: likwidacja praw i wolności w imię państwowego feminizmu, Dżenderowy geszeft, Transfery finansowe po feministycznemu), Bettina Röhl (Seksualne mity feminizmu, Strategia „gender mainstreaming)”, Stefan Sasse, (Idea emancypacji kobiet w historii), Matthias Heitmann (Polityka równości płci jako narzędzie władzy, Od ruchu kobiecego do „sfeminizowanego społeczeństwa”), Peter Beck (Kobiety w typie Rambo), Paul-Hermann Grune ( Kobiety i dzieci najpierw) , Björn Thorsten Leimbach (Żyć po męsku. Wzmocnienie męskości), Leila Bust (Żyć po kobiecemu. Zwrot ku kobiecości), Michail A. Xenos (Meduzie nie ofiarowuje się róż), Volker Zastrow (Dżender, czyli polityczne przekształcanie płci), prof. Manfred Spreng i Harald Seubert (Zgwałcenie ludzkiej tożsamości. O błędach ideologii dżender). Ważnymi postaciami niemieckiego antyfeminizmu są pisarze Bernhard Lassahn , autor książki Kobieta bez świata. Trylogia o ratowaniu miłości (dotychczas ukazała się część 1. Wojna przeciwko mężczyźnie, i część 2. Wojna przeciwko dziecku) oraz Wolfgang A. Gogolin autor satyrycznych powieści wyśmiewających absurdy systemu feministycznego."

print(get_key_words(s,5))