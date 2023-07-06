function defaultdict(defaultValue) {
  return new Proxy({}, {
    get: function(obj, prop) {
      if (!(prop in obj)) {
        obj[prop] = new Set();
      }
      return obj[prop];
    }
  });
}

function defaultdict(defaultValue) {
  return new Proxy({}, {
    get: function(obj, prop) {
      if (!(prop in obj)) {
        obj[prop] = defaultValue instanceof Function ? new defaultValue() : defaultValue;
      }
      return obj[prop];
    }
  });
}

