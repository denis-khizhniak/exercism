class ReverseString {

    String reverse(String inputString) {
        String result = "";
        for (int i = inputString.length()-1; i >= 0; i--) {
            char c = inputString.charAt(i);
            result += c;
        }
        return result;
    }

}
