from ceasar_cipher import encrypt_, decrypt_, break_cipher

def test_encrypt_normal():
  assert encrypt_('cat', 5) == "hfy"

def test_encrypt_bigkey20():
  assert encrypt_('cat', 20) == "wun"

def test_encrypt_bigkey26():
  assert encrypt_('cat', 26) == "cat"

def test_encrypt_bigkey27():
  assert encrypt_('cat', 27) == "dbu"

def test_encrypt_bigkey43():
  assert encrypt_('cat', 43) == "trk"

def test_encrypt_bigkey195():
  assert encrypt_('cat', 195) == "png"

def test_encrypt_Capital195():
  assert encrypt_('Cat', 195) == "png"

def test_encrypt_different_word():
  assert encrypt_('Snake', 7) == "zuhrl"

def test_encrypt_sentence_text():
  assert encrypt_('In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.', 7) == "pu h ovsl pu aol nyvbuk aolyl spclk h oviipa. uva h uhzaf, kpyaf, dla ovsl, mpsslk dpao aol lukz vm dvytz huk hu vvgf ztlss, uvy fla h kyf, ihyl, zhukf ovsl dpao uvaopun pu pa av zpa kvdu vu vy av lha: pa dhz h oviipa-ovsl, huk aoha tlhuz jvtmvya."

def test_decrypt__simple():
  assert decrypt_('hfy', 5) == 'cat'

def test_decrypt__text():
    assert decrypt_('pu h ovsl pu aol nyvbuk aolyl spclk h oviipa. uva h uhzaf, kpyaf, dla ovsl, mpsslk dpao aol lukz vm dvytz huk hu vvgf ztlss, uvy fla h kyf, ihyl, zhukf ovsl dpao uvaopun pu pa av zpa kvdu vu vy av lha: pa dhz h oviipa-ovsl, huk aoha tlhuz jvtmvya.', 7) == 'in a hole in the ground there lived a hobbit. not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort.'

def test_decrypt_bigkey195():
  assert decrypt_('png', 195) == 'cat'

def test_break_cipher_small_word():
  assert break_cipher('hfy') == 'cat'

def test_break_cipher_small_sentence():
  assert break_cipher("dcrt ndj zcdl paa iwt tatbtcih, xi'h cdi sxuuxrjai id ejaa idvtiwtg p htcitcrt") == "once you know all the elements, it's not difficult to pull together a sentence"

def test_break_cipher_notenglish():
  cipher = encrypt_('russkoeslovo', 145)
  assert break_cipher(cipher) == "Not English"

def test_break_cipher_notenglish2():
  cipher = encrypt_('привет', 145)
  assert break_cipher(cipher) == "Not English"

def test_break_cipher_text():
  text = 'In a hole in the ground there lived a hobbit. Not a nasty, dirty, wet hole, filled with the ends of worms and an oozy smell, nor yet a dry, bare, sandy hole with nothing in it to sit down on or to eat: it was a hobbit-hole, and that means comfort. It had a perfectly round door like a porthole, painted green, with a shiny yellow brass knob in the exact middle. The door opened on to a tube-shaped hall like a tunnel: a very comfortable tunnel without smoke, with panelled walls, and floors tiled and carpeted, provided with polished chairs, and lots and lots of pegs for hats and coats — the hobbit was fond of visitors. The tunnel wound on and on, going fairly but not quite straight into the side of the hill — The Hill, as all the people for many miles round called it — and many little round doors opened out of it, first on one side and then on another. No going upstairs for the hobbit: bedrooms, bathrooms, cellars, pantries (lots of these), wardrobes (he had whole rooms devoted to clothes), kitchens, dining-rooms, all were on the same floor, and indeed on the same passage. The best rooms were all on the left-hand side (going in), for these were the only ones to have windows, deep-set round windows looking over his garden, and meadows beyond, sloping down to the river. This hobbit was a very well-to-do hobbit, and his name was Baggins. The Bagginses had lived in the neighbourhood of The Hill for time out of mind, and people considered them very respectable, not only because most of them were rich, but also because they never had any adventures or did anything unexpected: you could tell what a Baggins would say on any question without the bother of asking him. This is a story of how a Baggins had an adventure, and found himself doing and saying things altogether unexpected. He may have lost the neighbours’ respect, but he gained — well, you will see whether he gained anything in the end. '

  cipher = encrypt_(text, 5)

  assert break_cipher(cipher) == text.lower()

def test_break_cipher_text2():
  text = 'Skilled readers and learners are constantly making connections: they recognize the interrelated nature of knowledge and actively note themes and similarities as they emerge. Students can learn how to make effective connections, and how to group these connections into three categories. Text-to-self connections relate ideas learned in a text with a student’s own experiences or ideas. Text-to-text connections are recurringwords or ideas within a book. Finally, text-to-world connections are links between ideas in a text and other domains of knowledge.'

  cipher = encrypt_(text, 3)
  assert cipher == 'vnloohg uhdghuv dqg ohduqhuv duh frqvwdqwob pdnlqj frqqhfwlrqv: wkhb uhfrjqlch wkh lqwhuuhodwhg qdwxuh ri nqrzohgjh dqg dfwlyhob qrwh wkhphv dqg vlplodulwlhv dv wkhb hphujh. vwxghqwv fdq ohduq krz wr pdnh hiihfwlyh frqqhfwlrqv, dqg krz wr jurxs wkhvh frqqhfwlrqv lqwr wkuhh fdwhjrulhv. whaw-wr-vhoi frqqhfwlrqv uhodwh lghdv ohduqhg lq d whaw zlwk d vwxghqw’v rzq hashulhqfhv ru lghdv. whaw-wr-whaw frqqhfwlrqv duh uhfxuulqjzrugv ru lghdv zlwklq d errn. ilqdoob, whaw-wr-zruog frqqhfwlrqv duh olqnv ehwzhhq lghdv lq d whaw dqg rwkhu grpdlqv ri nqrzohgjh.'

  assert break_cipher(cipher) == text.lower()

  cipher = encrypt_(text, 458)

  assert break_cipher(cipher) == text.lower()


def test_break_cipher_spanish():
  text = 'Si eres deportista y te gusta el agua puedes nadar, si te gusta la nieve puedes esquiar. Si no dispones de mucho tiempo puedes correr o ir en bicicleta.'
  cipher = encrypt_(text, 15)
  assert cipher == 'hx tgth stedgixhip n it vjhip ta pvjp ejtsth cpspg, hx it vjhip ap cxtkt ejtsth thfjxpg. hx cd sxhedcth st bjrwd ixtbed ejtsth rdggtg d xg tc qxrxratip.'
  assert break_cipher(cipher) == 'Not English'
