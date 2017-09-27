#Information Cryptography
import time

print ""
print ""
print "Loading InfoCrypt....."
time.sleep(3)
print ""

def options():

    print ""
    time.sleep(0.5)
    print "[r] *Reminder*"
    time.sleep(0.5)
    print "[c] Difference between Codes and Ciphers"
    time.sleep(0.5)
    print "[g] The 4 Goals of Cryptography"
    time.sleep(0.5)
    print "[w] What is Cryptography?"
    time.sleep(0.5)
    print "[s] Symmetric Cryptography"
    time.sleep(0.5)
    print "[a] Asymmetric Cryptography"
    time.sleep(0.5)
    print "[h] Hash functions"
    time.sleep(0.5)
    print "[d] Digital Signatures"
    time.sleep(0.5)
    print "(Type 'banner' to show banner.)"
    time.sleep(0.5)
    print "(Type 'q' to quit.)"
    time.sleep(0.5)
    print "(Type 'ls' to show options.)"
    time.sleep(0.5)

def whatiscrypt():
    print """
    ----------------------------------------------------------------------------

    [*] Cryptography: is that art of turning plaintext, into encrypted text. """

    time.sleep(5)

    print ""
    print """
    Cryptography...

    has 2 basic operations:

    [*] Encryption

    (Converts information from plaintext form into encrypted ciphertext)

    [*] Decryption

    (Converts information from encrypted ciphertext into plaintext form)

    [*] (Type 'ls' to show options)
    ----------------------------------------------------------------------------
    """

def remind():
    print ""
    print """
     *REMEMBER*

    - Never try to build your own encryption algorithm unless you really know
      what you're doing!

    - Use encrpytion algorithms proven to be secure!

    - The longer the key length, the more secure your information will be!
    - BUT as the key gets longer the Performance of the algorithm goes down!
    """

def banner():

    print """

                _________ _        _______  _______  _______  _______  _______ __________________ _______  _
                \__   __/( (    /|(  ____ \(  ___  )(  ____ )(       )(  ___  )\__   __/\__   __/(  ___  )( (    /|
                   ) (   |  \  ( || (    \/| (   ) || (    )|| () () || (   ) |   ) (      ) (   | (   ) ||  \  ( |
                   | |   |   \ | || (__    | |   | || (____)|| || || || (___) |   | |      | |   | |   | ||   \ | |
                   | |   | (\ \) ||  __)   | |   | ||     __)| |(_)| ||  ___  |   | |      | |   | |   | || (\ \) |
                   | |   | | \   || (      | |   | || (\ (   | |   | || (   ) |   | |      | |   | |   | || | \   |
                ___) (___| )  \  || )      | (___) || ) \ \__| )   ( || )   ( |   | |   ___) (___| (___) || )  \  |
                \_______/|/    )_)|/       (_______)|/   \__/|/     \||/     \|   )_(   \_______/(_______)|/    )_)
        ______                                   __                                                       __
       /      \                                 /  |                                                     /  |
      /$$$$$$  |  ______   __    __   ______   _$$ |_     ______    ______    ______   ______    ______  $$ |____   __    __
      $$ |  $$/  /      \ /  |  /  | /      \ / $$   |   /      \  /      \  /      \ /      \  /      \ $$      \ /  |  /  |
      $$ |      /$$$$$$  |$$ |  $$ |/$$$$$$  |$$$$$$/   /$$$$$$  |/$$$$$$  |/$$$$$$  |$$$$$$  |/$$$$$$  |$$$$$$$  |$$ |  $$ |
      $$ |   __ $$ |  $$/ $$ |  $$ |$$ |  $$ |  $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$/ /    $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |
      $$ \__/  |$$ |      $$ \__$$ |$$ |__$$ |  $$ |/  |$$ \__$$ |$$ \__$$ |$$ |     /$$$$$$$ |$$ |__$$ |$$ |  $$ |$$ \__$$ |
      $$    $$/ $$ |      $$    $$ |$$    $$/   $$  $$/ $$    $$/ $$    $$ |$$ |     $$    $$ |$$    $$/ $$ |  $$ |$$    $$ |
       $$$$$$/  $$/        $$$$$$$ |$$$$$$$/     $$$$/   $$$$$$/   $$$$$$$ |$$/       $$$$$$$/ $$$$$$$/  $$/   $$/  $$$$$$$ |
                          /  \__$$ |$$ |                          /  \__$$ |                   $$ |                /  \__$$ |
                          $$    $$/ $$ |                          $$    $$/                    $$ |                $$    $$/
                           $$$$$$/  $$/                            $$$$$$/                     $$/                  $$$$$$/

                                                       #InfoCrypt 0.1
                                                 [*].Crypt made simple.[*]
                                              [*]    Created By apt-get    [*]
                            [*]    Knowledge isn't power, but what you do with that Knowledge..is.   [*]

"""


def DES():
    print ""
    print """


    ---> DES (Data Encryption Standard) <--

    -DES uses an encryption operation called the Feistel function for 16 rounds of Encryption

    -Is no longer considered secure!

    >>>>> What you should know about DES <<<<<

    -Symmetric encryption algorithm

    -Block cipher opterating on 65-bit blocks

    -Key Length of 56 bits

    -Now considered insecure due to small Key Length



    """

def TDES():
    print ""
    print """

       ^^^ Triple DES (3DES) ^^^

    - 3 rounds of DES encryption / Applies DES to plaintext three times

    - Requires 3 keys

    - Double DES is no more secure than standard DES, due to the meet-in-the-middle attack.

    - 3DES is considered secure through 2030

    >>>>> Key facts to remember about 3DES <<<<<

    -Symmetric encryption algorithm

    -Block cipher operating on 64-bit blocks

    -Effective key length of 112 bits

    -Considered secure


    """

def AES():
    print ""
    print """


    ***** AES (Advanced Encryption Standard) *****

    - Uses Subsitution and Transposition

    - Symmetric encryption algorithm

    - Block cipher operating on 128-bit blocks

    - Ability to choose a Key length of 128, 192, or 256 bit key

    - Considered Secure



    """


def Blowfish():
    print ""
    time.sleep(1)
    print """
    ----------------------------------------------------------------------------
    ******** Blowfish ******

    - Is a public domain algorithm
    - Designed as a DES replacement / Created to replace DES
    - Uses a Feistel network
    - Combines substitution and transposition operastions

    -----Facts on Blowfish------

    - Symmetric encryption algorithm
    - Block cipher operating on 64-bit blocks
    - Key length anywhere between 32 and 448 bits
    - Not considered secure

    - RECOMENDED TO USE TWOFISH INSTEAD
    ----------------------------------------------------------------------------
    """

def Twofish():
    print ""
    time.sleep(1)
    print """


      ****** TWOFISH ******

    - Designed to replace DES

    - Placed into the public domain

    - Uses a Feistal network

    - that combineds Subsitution and Transposition

    --------- Key facts on Twofish ------------

    - Symmetric encryption algorithm

    - Block cipher operating on 128-bit blocks

    - Key length of 128, 192, or 256 bits

    - considered secure



    """

def RC4():
    print ""
    time.sleep(1)
    print """
    ------------------------------------------------------

    ######### RC4 Cryptographic Algorithm #########

    - Used in WEP (Wired Equivalent Privacy)

    - and Wi-Fi Protected Access (WPA)

    - Secure Sockets Layer (SSL)

    - Transport Layer Security (TLS) (Used to replace SSL)

    - No longer considered secure

    ------------- Key facts on RC4 ----------------

    - Symmetric encryption algorithm

    - Stream cipher

    - Variable length key between 40 bits nad 2,048 bts

    - Not considered secure

    ----------------------------------------------------

    """

def goalsofcrypt():
        print ""
        print """


        ******** THE 4 Goals of cryptograhpy *******

        1. Confidentiality

        [*] Confidentiality = Authorized access only

        2. Integrity

        [*] Integrity = No unauthorized changes

        3. Authentication

        [*] Authentication = Proof of identity claims

        4. Nonrepudiation

        [*] Nonrepudiation = Verifiable origin of a message

        [*] Digital signatures provide nonrepudiation

        [*] Nonrepudiation is only possible with asymmetric cryptography

        """


def Steganography():
    print ""
    time.sleep(1)
    print """


    ********** Steganography **************

    - Hides data in large files / Hides information in plain sight

    - Most common technique involves hiding text within an image file

    - The higher the resoluation in an image, the more space allowed to hide

    - A pixel or two may get shaded in but not visible to the naked eye

    - Images with embedded text may be posted in plain sight

    """

def optionssym():
    print ""
    print ""
    print "[0]. DES"
    time.sleep(0.5)
    print "[1]. 3DES"
    time.sleep(0.5)
    print "[2]. AES"
    time.sleep(0.5)
    print "[3]. Blowfish"
    time.sleep(0.5)
    print "[4]. Twofish"
    time.sleep(0.5)
    print "[5]. RC4"
    time.sleep(0.5)
    print "[6]. Steganography"
    print ""

def Hashfbanner():
    time.sleep(2)
    print """


           @@@           @@@  @@@   @@@@@@    @@@@@@   @@@  @@@           @@@
            @@@          @@@  @@@  @@@@@@@@  @@@@@@@   @@@  @@@          @@@
             @@!         @@!  @@@  @@!  @@@  !@@       @@!  @@@         @@!
              !@!        !@!  @!@  !@!  @!@  !@!       !@!  @!@        !@!
               @!!       @!@!@!@!  @!@!@!@!  !!@@!!    @!@!@!@!       @!!
                !!!      !!!@!!!!  !!!@!!!!   !!@!!!   !!!@!!!!      !!!
                 !!:     !!:  !!!  !!:  !!!       !:!  !!:  !!!     !!:
                  ::!    :!:  !:!  :!:  !:!      !:!   :!:  !:!    ::!
                   ::    ::   :::  ::   :::  :::: ::   ::   :::    ::
                    : :   :   : :   :   : :  :: : :     :   : :  : :


    @@@@@@@@  @@@  @@@   @@@@@@@  @@@  @@@  @@@@@@@  @@@   @@@@@@   @@@  @@@   @@@@@@
    @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@ @@@  @@@@@@@  @@@  @@@@@@@@  @@@@ @@@  @@@@@@@
    @@!       @@!  @@@  !@@       @@!@!@@@    @@!    @@!  @@!  @@@  @@!@!@@@  !@@
    !@!       !@!  @!@  !@!       !@!!@!@!    !@!    !@!  !@!  @!@  !@!!@!@!  !@!
    @!!!:!    @!@  !@!  !@!       @!@ !!@!    @!!    !!@  @!@  !@!  @!@ !!@!  !!@@!!
    !!!!!:    !@!  !!!  !!!       !@!  !!!    !!!    !!!  !@!  !!!  !@!  !!!   !!@!!!
    !!:       !!:  !!!  :!!       !!:  !!!    !!:    !!:  !!:  !!!  !!:  !!!       !:!
    :!:       :!:  !:!  :!:       :!:  !:!    :!:    :!:  :!:  !:!  :!:  !:!      !:!
     ::       ::::: ::   ::: :::   ::   ::     ::     ::  ::::: ::   ::   ::  :::: ::
     :         : :  :    :: :: :  ::    :      :     :     : :  :   ::    :   :: : :


"""

def Hashfoptions():

    print ""
    print "[0]. HMAC"
    time.sleep(0.5)
    print "[1]. MD5"
    time.sleep(0.5)
    print "[2]. SHA"
    time.sleep(0.5)
    print "[3]. RIPEMD"
    time.sleep(0.5)
    print ""

def Hashfunctions():
    Hashfbanner()
    time.sleep(0.5)
    print ""
    print """

      Hash functions are one-way functions that transform a variable length input
      into a unique, fixed-length output.

    - One-way functions / can't be reversed

    - The output of a hash function will always be the same length, regardless of
      the input size.

    - No two inputs to a hash function should produce the same output.



    ----- There are two ways that a hash function can fail -------



    1. If the hash function is reversible, it is not secure

    2. If they are not collision resistant


    """
    starth = raw_input("Press Enter to continue...")
    print ""
    print "[*] Please select an option.."
    time.sleep(0.5)
    print "(Type 'q' to quit > Hash Functions < )"
    time.sleep(0.5)
    print "(Type 'ls' to show list of commands)"
    time.sleep(0.5)
    print ""
    print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
    time.sleep(2)
    Hashfoptions()
    while True:
        userinput = raw_input("User@InfoCrypt: ")
        if userinput == "0":
            hashremem()
        elif userinput == "ls":
            Hashfoptions()
        elif userinput == "1":
            md5hash()
        elif userinput == "banner":
            Hashfbanner()
        elif userinput == "2":
            shahash()
        elif userinput == "3":
            ripehash()
        elif userinput == "q":
            print ""
            print "Going back.."
            time.sleep(1)
            print "Type 'ls' for options"
            print ""
            break
        else:
            print ""
            print "Unkown Command. Try Again.."
            print ""

def hashremem():
    time.sleep(0.5)
    print """



    -- HMAC --

    - One use of hash functions is in the Hash-Based Message Authentication Code.

    - HMAC combines symmetric cryptography and hashing

    - Provides authentication and integrity

    - Create and verify message authentication code by using a secret key in
    	conjunction with a hash function



    ** REMEMBER ***

    - Hash functions are used with asymmetric cryptography for digital signatures
      and digital certificates



    """
def shahash():
    time.sleep(0.5)
    print """


    -- SHA (Secure Hash Algorithm) --

    - - 3 - - - - - - - 6 - - - - - - - - - 9 -

    - SHA-1 -

    - Produces a 160-bit hash value

    - Contains security flaws that render it insecure

    -------------------------------------------------------------------------

    - SHA-2 -
      (Was made to replace SHA-1)

    - Consists of a family of six hash functions

    - Produces output of 224,256,384 and 512 bits

    - Uses a mathematically similar approach to SHA-1 and MD5

    - Still safe to use
    ------------------------------------------------------------------------

    - SHA-3 -

    - Designed as an eventual replacement for SHA-2

    - Uses a completely different hash generation approach than SHA-2

    - Produces hashes of user-selected fixed length

    ------------------------------------------------------------------------

    """
def md5hash():
    time.sleep(0.5)
    print """

    ----------------------------------------------------------------------------

    --MD5 (Message Digest 5)--

    - * Message Digest is Another word for Hash *

    - Created by Ron Rivest in 1991.

    - MD5 is the fifth in a series of hash functions.

    - MD5 replaced the MD4 algorithm after research showed that MD4 was insecure.

    - MD5 Produces a 128-bit hashes.

    - MD5 is no longer secure, and shouldn't be used.

    --------------------------------------------------------------------------

    """
def ripehash():
    time.sleep(0.5)
    print """

    -- RIPEMD (RACE Integrity Primitives Evaluation Message Digest ) --

    - Created as an alternative to government-sponsored hash functions

    - Produces 128,160,256, and 320-bit hashes

    - Contains flaws in the 128-bit version

    """
def CodesandCiphers():
    print ""
    print """
    ----------------------------------------------------------------------------

    >>>Codes and Ciphers<<<<

    -They are both two different things

    {

    -Code = A system that subsitutes one word or phrase for anonther. Codes
    	    are intended to provide secrecy and/or efficiency.

    (Ex.Police saying 10-4 meaning 'I acknowledge your message')

    }

    {

    -Ciphers = A system that uses mathematical algorithms to encrypt and decrypt
    		   messages.

    }

    ****Ciphers have two different ways of processing a message*****

    1. Stream Ciphers (Operate on one character, or bit, of a message at a time.)

    2. Block Ciphers (Operate on large segments of the message at the same time.)

    ----------------------------------------------------------------------------

    ### Ciphers prefrom their Encryption and decryption using 2 basic building blocks ###

    1. Subsitution Ciphers - (Change the characters in a message)

    Ex.1

    <Caesars Cipher>

    Replacing an 'A' with 'C'. 'ABC' Turns into 'CDE'. 'CDE' Taking the place of 'ABC'.

    Ex.2

    'abcdefghijklmnopqrstuvwtyz' -> 'cdefghijklmnopqrstuvwxyzab'

    The message 'Hello World' would become 'Jgnnq Yqtnf'

    2. Transposition Ciphers - (Rearrange the characters in a message) eg. "Hello" into "eHlol"

    """


def Digitalsig():
    print """

    -- Digital signatures --

    - Digital signatures use asymmetric cryptography to achieve intergrity,
    	authentication, and non-repudiation.

     * What Signed Message Recipients Know *

     1. The owner of the public key is the person who signed the message.
    	(Authentication)

     2. The message was not altered after being signed.
     	(Integrity)

    3. The recipient can prove these facts to a third party
       (Non-repudiation)


    --------------------What Digital Signatures Depend On -----------------------

    1. Collision-resistant hash functions

    2. Asymmetric cryptography

    -----------------------------------------------------------------------------

    - Use private keys to create digital signatures

    - Digitally signing messages does not provide Confidentiality.

    -----------------------------------------------------------------------------

    """

def Asymmetric():
    Asymmetricbanner()
    time.sleep(0.5)
    print ""
    print """

    -----Asymmetric Cryptography-----

    *Uses two keys

    -uses key pair

    Each user gets two keys

    -Public and Private Key

    *Public Key

    (Freely distributed to everyone with whom the user would like to commmunicate)

    *Private Key

    (Held in secret and don't disclose to anyone else)


    Ex. Bob and Jerry want to send a message to each other using Asymmetric
    	Cryptography. Bob uses his private key to encrypt the message, and
    	gives his public key over to Jerry, in order to decrypt the message.
    	Once it is decrypted, Jerry then uses his Private key to encrpyt the
    	message, as well as lending over his Public Key to Decrypt the message.

    """
    print "-Asymmetric Crytography is slower than Symmetric, but also more scalable."
    print ""
    print ""
    starts = raw_input("Press Enter to continue...")
    print """

    ****** RSA Cryptography *******

    -Asymmetric encryption algorithm
    -It uses Variable length keys between 1,024 and 4,096 bits
    -Considered secure

    ***PGP and GPG***

    ---PGP (Pretty Good Privacy)---

    - Uses public and private key pairs
    - Combines both symmetric and asymmetric crptography
    """
    print ""
    start = raw_input("Press Enter to continue...")
    print ""



#Both banners
def Asymmetricbanner():
    print """



       @@@@@@    @@@@@@   @@@ @@@  @@@@@@@@@@   @@@@@@@@@@   @@@@@@@@  @@@@@@@  @@@@@@@   @@@   @@@@@@@
      @@@@@@@@  @@@@@@@   @@@ @@@  @@@@@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@  @@@@@@@@
      @@!  @@@  !@@       @@! !@@  @@! @@! @@!  @@! @@! @@!  @@!         @@!    @@!  @@@  @@!  !@@
      !@!  @!@  !@!       !@! @!!  !@! !@! !@!  !@! !@! !@!  !@!         !@!    !@!  @!@  !@!  !@!
      @!@!@!@!  !!@@!!     !@!@!   @!! !!@ @!@  @!! !!@ @!@  @!!!:!      @!!    @!@!!@!   !!@  !@!
      !!!@!!!!   !!@!!!     @!!!   !@!   ! !@!  !@!   ! !@!  !!!!!:      !!!    !!@!@!    !!!  !!!
      !!:  !!!       !:!    !!:    !!:     !!:  !!:     !!:  !!:         !!:    !!: :!!   !!:  :!!
      :!:  !:!      !:!     :!:    :!:     :!:  :!:     :!:  :!:         :!:    :!:  !:!  :!:  :!:
      ::   :::  :::: ::      ::    :::     ::   :::     ::    :: ::::     ::    ::   :::   ::   ::: :::
       :   : :  :: : :       :      :      :     :      :    : :: ::      :      :   : :  :     :: :: :


 @@@@@@@  @@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@   @@@@@@    @@@@@@@@  @@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@ @@@
@@@@@@@@  @@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@  @@@@@@@@  @@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@ @@@
!@@       @@!  @@@  @@! !@@  @@!  @@@    @@!    @@!  @@@  !@@        @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@! !@@
!@!       !@!  @!@  !@! @!!  !@!  @!@    !@!    !@!  @!@  !@!        !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@! @!!
!@!       @!@!!@!    !@!@!   @!@@!@!     @!!    @!@  !@!  !@! @!@!@  @!@!!@!   @!@!@!@!  @!@@!@!   @!@!@!@!   !@!@!
!!!       !!@!@!      @!!!   !!@!!!      !!!    !@!  !!!  !!! !!@!!  !!@!@!    !!!@!!!!  !!@!!!    !!!@!!!!    @!!!
:!!       !!: :!!     !!:    !!:         !!:    !!:  !!!  :!!   !!:  !!: :!!   !!:  !!!  !!:       !!:  !!!    !!:
:!:       :!:  !:!    :!:    :!:         :!:    :!:  !:!  :!:   !::  :!:  !:!  :!:  !:!  :!:       :!:  !:!    :!:
 ::: :::  ::   :::     ::     ::          ::    ::::: ::   ::: ::::  ::   :::  ::   :::   ::       ::   :::     ::
 :: :: :   :   : :     :      :           :      : :  :    :: :: :    :   : :   :   : :   :         :   : :     :

"""

def Symmetricbanner():
    print """






            ::::::::  :::   ::: ::::    ::::  ::::    ::::  :::::::::: ::::::::::: :::::::::  ::::::::::: ::::::::
           :+:    :+: :+:   :+: +:+:+: :+:+:+ +:+:+: :+:+:+ :+:            :+:     :+:    :+:     :+:    :+:    :+:
           +:+         +:+ +:+  +:+ +:+:+ +:+ +:+ +:+:+ +:+ +:+            +:+     +:+    +:+     +:+    +:+
           +#++:++#++   +#++:   +#+  +:+  +#+ +#+  +:+  +#+ +#++:++#       +#+     +#++:++#:      +#+    +#+
                  +#+    +#+    +#+       +#+ +#+       +#+ +#+            +#+     +#+    +#+     +#+    +#+
           #+#    #+#    #+#    #+#       #+# #+#       #+# #+#            #+#     #+#    #+#     #+#    #+#    #+#
            ########     ###    ###       ### ###       ### ##########     ###     ###    ### ########### ########
 ::::::::  :::::::::  :::   ::: ::::::::: ::::::::::: ::::::::   ::::::::  :::::::::      :::     :::::::::  :::    ::: :::   :::
:+:    :+: :+:    :+: :+:   :+: :+:    :+:    :+:    :+:    :+: :+:    :+: :+:    :+:   :+: :+:   :+:    :+: :+:    :+: :+:   :+:
+:+        +:+    +:+  +:+ +:+  +:+    +:+    +:+    +:+    +:+ +:+        +:+    +:+  +:+   +:+  +:+    +:+ +:+    +:+  +:+ +:+
+#+        +#++:++#:    +#++:   +#++:++#+     +#+    +#+    +:+ :#:        +#++:++#:  +#++:++#++: +#++:++#+  +#++:++#++   +#++:
+#+        +#+    +#+    +#+    +#+           +#+    +#+    +#+ +#+   +#+# +#+    +#+ +#+     +#+ +#+        +#+    +#+    +#+
#+#    #+# #+#    #+#    #+#    #+#           #+#    #+#    #+# #+#    #+# #+#    #+# #+#     #+# #+#        #+#    #+#    #+#
 ########  ###    ###    ###    ###           ###     ########   ########  ###    ### ###     ### ###        ###    ###    ###

"""


def Symmetric():
    print ""
    print ""
    #print " ##################### SYMMETRIC CRYPTOGRAPHY #########################"
    Symmetricbanner()
    print """

    -------------------------Symmetric Cryptography-----------------------------

    *Uses ONE key to Encrypt and Decrypt*

    Ex. Bob and Jerry want to send a message to each other using Symmetric
    	Cryptography. Bob then creates a key called "Apple" that would be used
    	to Encrypt and Decrypt the message. He then lends over the key to
    	Jerry, so that he may Decrpyt the message.
    ----------------------------------------------------------------------------
    """
    starts = raw_input("Press Enter to continue....")
    print ""
    print "[*] Please Select an Option..."
    time.sleep(0.5)
    print "(Type 'q' to quit >Symmetric Cryptography< )"
    time.sleep(0.5)
    print "(Type 'ls'to show options)"
    print ""
    print "[*][*][*][*][*][*][*][*][*][*][*][*][*][*][*]"
    time.sleep(2)
    optionssym()
    print ""
    while True:
        Userinput = raw_input("User@InfoCrypt: ")
        if Userinput == "0":
            DES()
        elif Userinput == "1":
            TDES()
        elif Userinput == "2":
            AES()
        elif Userinput == "3":
            Blowfish()
        elif Userinput == "4":
            Twofish()
        elif Userinput == "5":
            RC4()
        elif Userinput == "6":
            Steganography()
        elif Userinput == "ls":
            optionssym()
        elif Userinput == "banner":
            Symmetricbanner()
        elif Userinput == "q":
            print ""
            print "Going Back..."
            time.sleep(1)
            print ("Type 'ls' for options")
            break
        else:
            print ""
            print "I don't know that command :("
            print ""


def main():
    banner()
    print ""
    print ""
    time.sleep(1)
    print "[*] Please Select an Option..."
    #Prints out options
    options()

    while True:
        print ""
        userinput = raw_input("User@InfoCrypt: ")
        if userinput == "s":
            time.sleep(2)
            Symmetric()
        elif userinput == "a":
            Asymmetric()
        elif userinput == "q":
            print ""
            print "[*] Quitting..."
            time.sleep(1)
            exit
            break
        elif userinput == "banner":
            banner()
        elif userinput == "w":
            whatiscrypt()
        elif userinput == "ls":
            options()
        elif userinput == "g":
            goalsofcrypt()
        elif userinput == "c":
            CodesandCiphers()
        elif userinput == "r":
            remind()
        elif userinput == "h":
            Hashfunctions()
        elif userinput == "d":
            Digitalsig()
        else:
            print ""
            print "Do you even r00t bro? Please try again..."



main()
