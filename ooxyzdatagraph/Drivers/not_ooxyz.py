# Original code by Luke Schultz, with some ChatGPT, 2023
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def plot_data(x, y, z):
    """
    Plots the data on a 3D scatter plot

    Parameters:
        x (list): The x coordinates (fingerprint size)
        y (list): The y coordinates (min chunk size)
        z (list): The z coordinates (deduplication ratio)
    """

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    sc = ax.scatter(x, y, z, c=z, cmap=cm.turbo)
    fig.colorbar(sc, pad=0.2)

    ax.set_xlabel('Fingerprint Size (bytes)')
    ax.set_ylabel('Min Chunk Size (bytes)')
    ax.set_zlabel('Deduplication Ratio')
    ax.set_title('Deduplication Ratio vs.\nFingerprint Size and Min Chunk Size')

    plt.savefig("Output/driver04_not_ooxyz.png")


def main():
    l = [
            [ 2,8,0.734476430446705 ],
            [ 2,16,0.43203938459080216 ],
            [ 2,32,0.24580124111906576 ],
            [ 2,64,0.14842752956377225 ],
            [ 2,128,0.11097727339445394 ],
            [ 2,256,0.11472407399457296 ],
            [ 2,512,0.17168602405571562 ],
            [ 2,1024,0.31207883644456497 ],
            [ 8,4096,0.19551313607595203 ],
            [ 8,8192,0.28598164816611404 ],
            [ 8,16384,0.41334455245850454 ],
            [ 8,32768,0.5927319813183621 ],
            [ 8,65536,0.9991749710584448 ],
            [ 13,4096,0.3183068102011553 ],
            [ 13,8192,0.3299033963113852 ],
            [ 13,16384,0.3606354983765106 ],
            [ 13,32768,0.43796160420341035 ],
            [ 13,65536,0.9991749710584448 ]
        ]

    x = []
    y = []
    z = []
    for i in l:
        assert (len(i) == 3), "Wrong format xyz"
        x.append(i[0])
        y.append(i[1])
        z.append(i[2])
    plot_data(x, y, z)

if __name__ == "__main__":
    main()


