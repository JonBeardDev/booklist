<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Books</h1>
        <hr />
        <br /><br />
        <alert :message="message" v-if="showMessage"></alert>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal"
        >
          Add Book
        </button>
        <br /><br />
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Title</th>
              <th scope="col">Author</th>
              <th scope="col">Date Published</th>
              <th scope="col">Read?</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(book, index) in books" :key="index">
              <td>{{ book.title }}</td>
              <td>{{ book.author }}</td>
              <td>{{ book.date }}</td>
              <td>
                <span v-if="book.read">Yes</span>
                <span v-else>No</span>
              </td>
              <td>
                <div class="btn-group" role="group">
                  <button
                    type="button"
                    class="btn btn-warning btn-sm mx-2"
                    @click="toggleEditBookModal(book)"
                  >
                    Update
                  </button>
                  <button
                    type="button"
                    class="btn btn-danger btn-sm mx-2"
                    @click="handleDeleteBook(book)"
                  >
                    Delete
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- add new book modal -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new book</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddBookModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookTitle"
                  v-model="addBookForm.title"
                  placeholder="Enter title"
                />
              </div>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addBookForm.author"
                  placeholder="Enter author"
                />
              </div>
              <div class="mb-3">
                <label for="addBookDate" class="form-label"
                  >Date Published:</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="addBookDate"
                  v-model="addBookForm.date"
                  placeholder="Enter date published"
                />
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addBookRead"
                  v-model="addBookForm.read"
                />
                <label class="form-check-label" for="addBookRead">Read?</label>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm me-2"
                  @click="handleAddSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm mx-2"
                  @click="handleAddReset"
                >
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>

    <!-- edit book modal -->
    <div
      ref="editBookModal"
      class="modal fade"
      :class="{ show: activeEditBookModal, 'd-block': activeEditBookModal }"
      tabindex="-1"
      role="dialog"
    >
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Update</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleEditBookModal"
            >
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="editBookTitle" class="form-label">Title:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookTitle"
                  v-model="editBookForm.title"
                  placeholder="Enter title"
                />
              </div>
              <div class="mb-3">
                <label for="editBookAuthor" class="form-label">Author:</label>
                <input
                  type="text"
                  class="form-control"
                  id="editBookAuthor"
                  v-model="editBookForm.author"
                  placeholder="Enter author"
                />
              </div>
              <div class="mb-3">
                <label for="editBookDate" class="form-label"
                  >Date Published:</label
                >
                <input
                  type="text"
                  class="form-control"
                  id="editBookDate"
                  v-model="editBookForm.date"
                  placeholder="Enter date published"
                />
              </div>
              <div class="mb-3 form-check">
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="editBookRead"
                  v-model="editBookForm.read"
                />
                <label class="form-check-label" for="editBookRead">Read?</label>
              </div>
              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleEditSubmit"
                >
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleEditCancel"
                >
                  Cancel
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeEditBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from "axios";
import Alert from "./Alert.vue";

export default {
  data() {
    return {
      activeAddBookModal: false,
      addBookForm: {
        title: "",
        author: "",
        date: "",
        read: [],
      },
      activeEditBookModal: false,
      editBookForm: {
        title: "",
        author: "",
        date: "",
        read: [],
      },
      books: [],
      message: "",
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    addBook(payload) {
      const path = "http://localhost:5000/books";
      axios
        .post(path, payload)
        .then(() => {
          this.getBooks();
          this.message = "Book added!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getBooks();
        });
    },
    updateBook(payload, bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .put(path, payload)
        .then(() => {
          this.getBooks();
          this.message = "Book updated!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    removeBook(bookID) {
      const path = `http://localhost:5000/books/${bookID}`;
      axios
        .delete(path)
        .then(() => {
          this.getBooks();
          this.message = "Book removed!";
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getBooks();
        });
    },
    getBooks() {
      const path = "http://localhost:5000/books";
      axios
        .get(path)
        .then((res) => {
          this.books = res.data.books;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddReset() {
      this.initForm();
    },
    handleAddSubmit() {
      this.toggleAddBookModal();
      let read = false;
      if (this.addBookForm.read[0]) {
        read = true;
      }
      const payload = {
        title: this.addBookForm.title,
        author: this.addBookForm.author,
        date: this.addBookForm.date,
        read, // property shorthand
      };
      this.addBook(payload);
      this.initForm();
    },
    handleEditSubmit() {
      this.toggleEditBookModal(null);
      let read = false;
      if (this.editBookForm.read) read = true;
      const payload = {
        title: this.editBookForm.title,
        author: this.editBookForm.author,
        date: this.editBookForm.date,
        read,
      };
      this.updateBook(payload, this.editBookForm.id);
    },
    handleEditCancel() {
      this.toggleEditBookModal(null);
      this.initForm();
      this.getBooks();
    },
    handleDeleteBook(book) {
      this.removeBook(book.id);
    },
    initForm() {
      this.addBookForm.title = "";
      this.addBookForm.author = "";
      this.addBookForm.date = "";
      this.addBookForm.read = [];
      this.editBookForm.id = "";
      this.editBookForm.title = "";
      this.editBookForm.author = "";
      this.editBookForm.date = "";
      this.editBookForm.read = [];
    },
    toggleAddBookModal() {
      const body = document.querySelector("body");
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
    toggleEditBookModal(book) {
      if (book) {
        this.editBookForm = book;
      }
      const body = document.querySelector("body");
      this.activeEditBookModal = !this.activeEditBookModal;
      if (this.activeEditBookModal) {
        body.classList.add("modal-open");
      } else {
        body.classList.remove("modal-open");
      }
    },
  },
  created() {
    this.getBooks();
  },
};
</script>
