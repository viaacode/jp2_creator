from subprocess import check_output, STDOUT


def convert(source_file, destination_file, extra_options):
    try:
        tojp2(source_file, destination_file, extra_options)
    except Exception as e:
        uncompress(source_file)
        tojp2(source_file + "_uncompressed.tif", destination_file, extra_options)

def uncompress(source_file):
    output = check_output(["convert",
                           source_file,
                           "+compress",
                           source_file + "_uncompressed.tif"], stderr=STDOUT)

def tojp2(source_file, destination_file, extra_options):
    output = check_output(["kdu_compress",
                       "-i", source_file,
                       "-o", destination_file,
                       extra_options,
                       "Clevels=5",
                       "Cblk={64,64}",
                       "Corder=RPCL",
                       "Stiles={1024,1024}",
                       "Clayers=12",
                       "-rate", "-,2.5"], stderr=STDOUT)