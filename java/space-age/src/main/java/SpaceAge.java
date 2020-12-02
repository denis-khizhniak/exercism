class SpaceAge {

    double ageSeconds;

    public static final double EARTH_ORBITAL_PERIOD = 31557600;
    public static final double MERCURY_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 0.2408467;
    public static final double VENUS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 0.61519726;
    public static final double MARS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 1.8808158;
    public static final double JUPITER_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 11.862615;
    public static final double SATURN_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 29.447498;
    public static final double URANUS_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 84.016846;
    public static final double NEPTUNE_ORBITAL_PERIOD = EARTH_ORBITAL_PERIOD * 164.79132;

    SpaceAge(double seconds) {
        this.ageSeconds = seconds;
    }

    double getSeconds() {
        return this.ageSeconds;
    }

    double onEarth() {
        return this.ageSeconds / EARTH_ORBITAL_PERIOD;
    }

    double onMercury() {
        return this.ageSeconds / MERCURY_ORBITAL_PERIOD;
    }

    double onVenus() {
        return this.ageSeconds / VENUS_ORBITAL_PERIOD;
    }

    double onMars() {
        return this.ageSeconds / MARS_ORBITAL_PERIOD;
    }

    double onJupiter() {
        return this.ageSeconds / JUPITER_ORBITAL_PERIOD;
    }

    double onSaturn() {
        return this.ageSeconds / SATURN_ORBITAL_PERIOD;
    }

    double onUranus() {
        return this.ageSeconds / URANUS_ORBITAL_PERIOD;
    }

    double onNeptune() {
        return this.ageSeconds / NEPTUNE_ORBITAL_PERIOD;
    }

}
