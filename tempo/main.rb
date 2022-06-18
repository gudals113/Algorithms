
def convert (par)
    puts par.strip.reverse.upcase
    # in.reverse
end

convert("   tekramngnaad   ") == "DAANGNMARKET" # true
convert("   torrak         ") == "KARROT" # true
convert("   remmus         ") == "SUMMER" # true


