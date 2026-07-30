class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs: 
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0
        
        while i < len(s):
            # Trova l'indice del prossimo carattere '#' a partire da 'i'
            j = s.find('#', i)
            
            # Estrai la lunghezza della parola (tutto ciò che sta tra i e j)
            length = int(s[i:j])
            
            # La parola vera e propria inizia subito dopo il '#' e dura 'length' caratteri
            word_start = j + 1
            word_end = word_start + length
            
            result.append(s[word_start:word_end])
            
            # Aggiorna l'indice 'i' per puntare all'inizio del prossimo blocco
            i = word_end
            
        return result