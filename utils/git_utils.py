def patch_repo(url, dir, cwd, path=None, args=None, whitespace_fix=False, quiet=False):
    """
    Function to patch a repo with specified arguments.
    
    Args:
        url (str): URL of the repo.
        dir (str): Directory to download the repo.
        cwd (str): Current working directory.
        args (list, optional): List of arguments for the 'git apply' command.
        whitespace_fix (bool, optional): Whether to apply the '--whitespace=fix' argument.
        
    Returns:
        CompletedProcess: Completed process.
    """
    
    # Check if url, dir and cwd are strings
    if not isinstance(url, str) or not isinstance(dir, str) or not isinstance(cwd, str):
        raise ValueError("'url', 'dir' and 'cwd' must be strings")
    
    # Check if args is a list or None
    if args is not None and not isinstance(args, list):
        raise ValueError("'args' must be a list of strings or None")

    # Check if whitespace_fix is a boolean
    if not isinstance(whitespace_fix, bool):
        raise ValueError("'whitespace_fix' must be a boolean")
    
    os.makedirs(dir, exist_ok=True)

    filename = ""
    
    if url:
        filename = urlparse(url).path.split('/')[-1].replace('.git', '')
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(os.path.join(dir, filename), 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        except Exception as e:
            if not quiet:
                print(f"Error downloading from {url}. Error: {str(e)}")
            return
    elif path:
        filename = os.path.basename(url)
    
    if not path:
        path = os.path.join(dir, filename)

    cmd = ['git', 'apply']
    if whitespace_fix:
        cmd.append('--whitespace=fix')
    if args:
        cmd.extend(args)
    cmd.append(path)
    
    try:
        return subprocess.run(cmd, cwd=cwd, check=True)
    except subprocess.CalledProcessError as e:
        if not quiet:
            cprint(f"Error applying patch. Error: {str(e)}", color="flat_red")
