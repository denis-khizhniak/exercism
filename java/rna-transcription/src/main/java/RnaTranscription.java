import java.util.Map;
import java.util.HashMap;

class RnaTranscription {

    String transcribe(String dnaStrand) {
        Map<Character, Character> dnaRnaMap = new HashMap<Character, Character>() {
            {
                put('G', 'C');
                put('C', 'G');
                put('T', 'A');
                put('A', 'U');
            }
        };

        String result = "";
        for (int i = 0; i < dnaStrand.length(); i++) {
            char c = dnaStrand.charAt(i);
            result += dnaRnaMap.get(c);
        }

        return result;
    }

}
