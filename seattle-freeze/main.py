import geo_streaming
import analysis
import locations


def main():
    geo_streaming.create_stream(locations.HOUSTON)


if __name__ == "__main__":
    main()