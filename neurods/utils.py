import numpy as np

def url_to_interact(url, url_type='data8'):
    """Create an interact link from a URL in github or data-8.org.

    Parameters
    ----------
    url : string
        The URL of the file/folder you want to convert to an interact link.
    url_type : one of 'ds8' | 'data8'
        Whether the output URL should be attached to ds8 or data8.
    """
    # First define the repo name
    if not any([i in url for i in ['data-8', 'data8.org']]):
        raise ValueError('Provide a URL attached to a data-8 repository')
    if 'github.com' in url:
        repo_split = 'data-8/'
    elif 'data8.org' in url:
        repo_split = 'data8.org/'
    else:
        raise ValueError('Provide a URL for github.com or data8.org')
    repo = url.split(repo_split)[-1].split('/')[0]

    # Now pull file path/name
    name_split = 'gh-pages/' if 'github.com' in url else repo + '/'
    name = url.split(name_split)[-1]

    url_int = 'https://{2}.berkeley.edu/hub/interact?repo={0}&path={1}'.format(
        repo, name, url_type)
    print('Your interactive URL is:\n---\n{0}\n---'.format(url_int))
    return url_int
