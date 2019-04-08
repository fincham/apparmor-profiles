# Paths will need adjusting in this depending on how it's installed. cgit doesn't need much!

#include <tunables/global>

/usr/lib/cgit/cgit.cgi {
  #include <abstractions/base>

  /etc/cgitrc r,

  /srv/git/ r,
  /srv/git/** r,

  /srv/www/sources r,
  /srv/www/sources/** r,

  /opt/hotplate/git/cgit/filters/about Cx -> about,
  /opt/hotplate/git/cgit/filters/source Cx -> source,

  /bin/gzip rix,
  /bin/bzip2 rix,

  profile about {
    #include <abstractions/base>
    #include <abstractions/bash>
    #include <abstractions/perl>

    /bin/bash mrix,

    /opt/hotplate/git/cgit/filters/about r,
    /usr/bin/markdown rix,
    /bin/cat rix,

    # and some crap that bash wants to touch but doesn't need to
    deny /dev/tty rwx,
    deny /etc/nsswitch.conf rwx,
    deny /etc/passwd rwx,
  }

  profile source {
    #include <abstractions/base>
    #include <abstractions/bash>

    /bin/bash mrix,

    /opt/hotplate/git/cgit/filters/source r,
    /bin/sed rix,

    # and some crap that bash wants to touch but doesn't need to
    deny /dev/tty rwx,
    deny /etc/nsswitch.conf rwx,
    deny /etc/passwd rwx,
  }

  deny /etc/passwd rwx,
  deny /etc/nsswitch.conf rwx,
}
