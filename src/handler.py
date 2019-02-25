from Utils.processor import liquid_in_the_given_glass
import argparse
import json

def setupRun(volume, row, glass):
        print("For volume:", volume, "ml   rows:",row, "    glass :",glass)
        result = liquid_in_the_given_glass(int(volume), int(row), int(glass))
        print("result : ", json.dumps(result, indent=2, sort_keys=True))
        return result




def main():
    arger = argparse.ArgumentParser()

    arger.add_argument("-k", "--vol", dest="volume")
    arger.add_argument("-i", "--rows", dest="rows")
    arger.add_argument("-j", "--glass", dest="glass")

    opts = arger.parse_args()
    setupRun(opts.volume, opts.rows, opts.glass)

if __name__ == '__main__':
    main()