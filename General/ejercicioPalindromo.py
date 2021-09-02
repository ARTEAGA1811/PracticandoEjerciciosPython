

def remover_caracter(s, n):
  inicio = 0
  fin = len(s)
  resultado = s[inicio:n] + s[n+1:fin]
  return resultado

def solucion(cadena):
  if(len(cadena) == 0):
    return True
  else:
    for k in range(len(cadena)):
      subCadena = remover_caracter(cadena, k)
      igual, aux = 0, 0
      for ind in reversed(range(0, len(subCadena))):
        if subCadena[ind].lower() == subCadena[aux].lower():
          igual += 1
        aux += 1
      if len(subCadena) == igual:
        return True
    
    return False


def testear():
    # casosPrueba = [
    #   'raceacar',
    #   'Abccdba',
    #   'Abcdefdba',
    #   '',
    #   'A',
    #   'Ab'
    #   ]

    casosPrueba = [
      'gveilrcbbktuhbtjdkwbgkwrxoltirxtbyfhsbmuoxixvnoidnxdfjunlwqnxdcialvuzbxlxgckmtoxdnfuygsuomtlkmqyrysxlvfdenmliwqmtjgcdxwmybfbssztnwkyyjqryscnvanqhcjnmpecuwapxivgacpdkiqucycvlrhwcvyyxrhjrqnhdxmldxwafigkijptrornrwtkpbssmwmittinzpetkfszeycftqoshxxhddazdapzjycvjjqlybhfcqiizsceqkycspkefdmhgtkdjzrypxdekirmggjgxkwkktmdncpqflactlrlnjrdwtnhojvmzqpljawdhbihbedvubmunidlwbjfogacropoueyjxunndejeprbyobuwomrqeycgqnlzqgilvrroibhigdrzliglblbdchzyetcpvyibvzfeacnbkiiwvnmgsgdpsewwfdjkcbaelvhcerimtqrecmiozptxngkjnzwgnhrkuiobdbvrknuvzyfgwwiskxapzvyjvyeohkfgujndhhfkrfpbbftshwvhilgvcfsrxuakrytfmrwshvsqzenkydebrfwoycnvmmxsdhkebyapgthudqjvnwpwwfbzsqqnkzuisndetqytjajwxjxkrwrxkdwqharaikyksxbfjaofmhsmjttocsnzgqadpqoifhlxyxevrgkpkjqiboktafkrdefrthdmruvwjgeqdauzbpymcuzftofolqestobheaahsokvxyzbztavndtgpvmmhhwcpvdknvbvvqjrqpvafxicpnxjqpnafmhrxalfmyimqpvqodxrytvxfqucsinfdgzbpbpohjxoakjjgafwmhutrxyivrxvvfpjczlwodelknbxgoavptkmvofuldokpoboznmljlhmsmaarotjzsivbirrfptkdimpbenmsdeobpdlebjpduymsamwxrdpotvvchojkcceoogmeyzajysffsyjazyemgooecckjohcvvtopdrxwmasmyudpjbeldpboedsmnebpmidktpfrribviszjtoraamsmhljlmnzobopkodlufovmktpvaogxbnkledowlzcjpfvvxrviyxrtuhmwfagjjkaoxjhopbpbzgdfniscuqfxvtyrxdoqvpqmiymflaxrhmfanpqjxnpcixfavpqrjqvvbvnkdvpcwhhmmvpgtdnvatzbzyxvkoshaaehbotseqlofotfzucmypbzuadqegjwvurmdhtrfedrkfatkobiqjkpkgrvexyxlhfioqpdaqgznscottjmshmfoajfbxskykiarahqwdkxrwrkxjxwjajtyqtednsiuzknqqszbfwwpwnvjqduhtgpaybekhdsxmmvncyowfrbedyknezqsvhswrmftyrkauxrsfcvglihvwhstfbbpfrkfhhdnjugfkhoeyvjyvzpaxksiwwgfyzvunkrvbdboiukrhngwznjkgnxtpzoimcerqtmirechvleabckjdfwwespdgsgmnvwiikbncaefzvbiyvpcteyzhcdblblgilzrdgihbiorrvligqzlnqgcyeqrmowuboybrpejednnuxjyeuoporcagofjbwldinumbuvdebhibhdwajlpqzmvjohntwdrjnlrltcalfqpcndmtkkwkxgjggmrikedxpyrzjdktghmdfekpscykqecsziiqcfhbylqjjvcyjzpadzaddhxxhsoqtfcyezsfktepznittimwmssbpktwrnrortpjikgifawxdlmxdhnqrjhrxyyvcwhrlvcycuqikdpcagvixpawucepmnjchqnavncsyrqjyykwntzssbfbymwxdcgjtmqwilmnedfvlxsyryqmkltmousgyufndxotmkcgxlxbzuvlaicdxnqwlnujfdxndionvxixoumbshfybtxritloxrwkgbwkdjtbhutkbbcrlievgu','aba', 'annal', 'arras', 'array', 'assay', 'attar', 'belle', 'Bette',
      'boffo', 'boobs', 'booby', 'calla', 'cirri', 'deeds', 'ebbed', 'effed', 'egged', 'erred',
      'freer', 'gamma', 'Greer', 'Hakka', 'Hanna', 'Hesse', 'hooch', 'innit', 'Janna', 'Jesse', 'kappa', 
      'kooks', 'kooky', 'Lassa', 'lemme', 'Lippi', 'lotto', 'manna', 'motto', 'Nikki', 'noons', 'peeps', 'poops', 
      'ragga', 'recce', 'Rocco', 'Rollo', 'seeds', 'seeks', 'seems', 'seeps', 'seers', 'sells', 'setts', 'shoos',
      'sills', 'teeth', 'tooth', 'toots', 'tweet', 'villi', 'walla', 'wanna', 'yobbo', 'yukky', 'yummy', 
      'Zappa', 'Zorro']
       
    salidas = [True, True, False, True, True, True]
    for i in range(len(casosPrueba)):
        solution = None
        try:
            solution = solucion(casosPrueba[i])
            assert solution == False
            print("ta bien")
        except Exception as error:
            print(f"Error, test {casosPrueba[i]}, expected {False}, calculated {solution}", error)

testear()