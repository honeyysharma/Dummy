def main(argv):
    layerOrderFile = ""
    compScriptFile = ""
    try:
        opts, args = getopt.getopt(argv, "hl:c:", ["lfile=", "cfile="])
    except getopt.GetoptError:
        print 'YamlTest.py -l <layerOrderFile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print """ This scripts builds your comp script \n
 -l = Layer_order file
 -c = Comp Script (optional, if running from shot the pick Comp.nk)
 -h = Help for this script"""
            sys.exit()
        elif opt in ("-l", "--lfile"):
            layerOrderFile = arg
        elif opt in ("-c", "--cfile"):
            compScriptFile = arg

    if layerOrderFile == "":
        print "Please pass layer order file"
        sys.exit()
    print "-l: " + layerOrderFile
    if compScriptFile == "":
        compScriptFile = "comp.nk"
    print "-c: " + compScriptFile

if __name__ == "__main__":
    main(sys.argv[1:])
