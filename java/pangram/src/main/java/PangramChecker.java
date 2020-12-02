public class PangramChecker {

    public boolean isPangram(String input) {
        char[] alphabet = "abcdefghijklmnopqrstuvwxyz".toCharArray();
        for (char c : alphabet) {
            if (input.toLowerCase().indexOf(c) == -1) return false;
        }
        return true;
    }

}
