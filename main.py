import argparse
import personal.personal as m_psn

psn = m_psn.Personal()

"""
Configure Command Line Parsing Options
"""
parser = argparse.ArgumentParser(description='Load Personal Data')
parser.add_argument('--file', dest='filepath', help='Fully qualified file path to the personal data file to \
see supported formats try --help-formats')
parser.add_argument('--ff', dest='fformat', help='The file format being loaded if not specified will try to \
auto determine from file extension. To see available formats specify --help_ff')
parser.add_argument('--df', dest='dformat', default='raw', help='The display format to use if not specified will default \
to showing raw data. To see available display formats specify --help_df')
parser.add_argument('--help_ff', dest='helpFFormats', help='Shows available file formats', action="store_true")
parser.add_argument('--help_df', dest='helpDFormats', help='Shows available display formats', action="store_true")
args = parser.parse_args()

"""
Check and Execute Command Line Parameters
"""
if args.helpFFormats:
    types = ' '.join(psn.loader.registered_formats)
    print('\nValid file formats are ({}) specify with --ff option'.format(types))

if args.helpDFormats:
    print('\nValid display formats are (raw|pretty) specify with --df option')

if args.filepath:
    print('Attempting to load file {}'.format(args.filepath))
    if args.fformat:
        psn.loadPersonalData(args.filepath, args.fformat)
    else:
        psn.loadPersonalData(args.filepath, 'auto')

    psn.displayPersonalData(psn.loader.detectFormat(args.filepath), args.dformat)

