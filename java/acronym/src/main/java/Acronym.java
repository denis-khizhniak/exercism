import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.List;
import java.util.ArrayList;
import java.util.stream.Collectors;

class Acronym {

    String phrase;

    Acronym(String phrase) {
        this.phrase = phrase;
    }

    String get() {
        List<String> allMatches = new ArrayList<String>();
        Matcher m = Pattern.compile("[A-Za-z0-9']+")
            .matcher(this.phrase);
        while (m.find()) {
            allMatches.add(m.group());
        }
        return String.join("", allMatches.stream()
                .map(s -> s.replaceAll("^'|'$", "").substring(0, 1).toUpperCase())
                .collect(Collectors.toList()));
    }

}
