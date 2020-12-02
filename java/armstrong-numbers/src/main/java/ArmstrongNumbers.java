class ArmstrongNumbers {

    boolean isArmstrongNumber(int numberToCheck) {

        String numberToCheckString = Integer.toString(numberToCheck);
        int sum = 0;
        for (int i = 0; i < numberToCheckString.length(); i++) {
            sum += Math.pow(Character.getNumericValue(numberToCheckString.charAt(i)), numberToCheckString.length());
        }

        return sum == numberToCheck;
    }

}
