from subprocess import check_output, STDOUT


def convert(source_file, destination_file, extra_options):
    output = check_output(["kdu_compress",
                           "-i", source_file,
                           "-o", destination_file,
                           extra_options,
                           "Clevels=5",
                           "Cblk={64,64}",
                           "Cprecincts={256,256},{256,256},{128,128}",
                           "Creversible=yes",
                           "Cuse_sop=yes",
                           "Corder=LRCP",
                           "ORGgen_plt=yes",
                           "ORGtparts=R",
                           "-rate", "-,1,0.5,0.25"], stderr=STDOUT)
