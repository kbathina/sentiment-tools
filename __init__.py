# import pkg_resources

# resource_package = __name__  # Could be any module/package name
# resource_path = '/'.join(('templates', 'temp_file'))  # Do not use os.path.join()
# template = pkg_resources.resource_string(resource_package, resource_path)
# # or for a file-like stream:
# template = pkg_resources.resource_stream(resource_package, resource_path)


from sentiment_tools import custom_vader

from sentiment_tools import Anew

from sentiment_tools import OpinionFinder

from sentiment_tools import GPOMS

from sentiment_tools import Afinn