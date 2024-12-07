import logging
import time
import string
import multiprocessing
import codecs

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")


def rot13(s):
    return codecs.encode(s, "rot_13")


def process_a(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "EXIT":
            break
        message = message.lower()
        logging.info(f"Process A: Converted to lowercase: {message}")
        output_queue.put(message)
        time.sleep(5)  # Simulate delay


def process_b(input_queue, output_queue):
    while True:
        message = input_queue.get()
        if message == "EXIT":
            break
        encoded_message = rot13(message)
        logging.info(f"Process B: Encoded message using rot13: {encoded_message}")
        output_queue.put(encoded_message)


def main():
    queue_a_to_b = multiprocessing.Queue()
    queue_b_to_main = multiprocessing.Queue()

    process_a_instance = multiprocessing.Process(
        target=process_a, args=(queue_a_to_b, queue_b_to_main)
    )
    process_b_instance = multiprocessing.Process(
        target=process_b, args=(queue_a_to_b, queue_b_to_main)
    )

    process_a_instance.start()
    process_b_instance.start()

    try:
        while True:
            message = input("Enter message for process A (or 'exit' to quit): ")
            if message.lower() == "exit":
                break
            queue_a_to_b.put(message)

            if not queue_b_to_main.empty():
                result = queue_b_to_main.get()
                logging.info(f"Main process received: {result}")
    except KeyboardInterrupt:
        pass

    logging.info("Exiting main process")

    process_a_instance.terminate()
    process_b_instance.terminate()

    logging.info("Main process exiting")


if __name__ == "__main__":
    main()
